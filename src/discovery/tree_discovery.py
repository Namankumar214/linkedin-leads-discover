"""Tree-based profile discovery with deduplication"""

import asyncio
from typing import List, Set, Dict
from collections import deque
from linkdapi import AsyncLinkdAPI
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.console import Console, Group
from rich.panel import Panel
from rich.live import Live
from src.api.client import LeadsAPIClient

console = Console()


class ProfileTreeDiscovery:
    """Handles tree-based discovery of similar profiles"""

    def __init__(self, api_client: LeadsAPIClient, max_concurrent: int = 10):
        self.api_client = api_client
        self.max_concurrent = max_concurrent
        self.discovered_profiles: List[Dict] = []
        self.seen_urns: Set[str] = set()
        self.failed_usernames: List[str] = []
        self.failed_urns: List[str] = []
        self.log_buffer = deque(maxlen=30)
        self.live_display = None
        self.progress = None
        self.profile_lock = asyncio.Lock()  # Lock for thread-safe profile additions

    def _add_log(self, message: str):
        """Add message to log buffer and update display"""
        self.log_buffer.append(message)
        if self.live_display and self.progress:
            try:
                self.live_display.update(Group(self._get_status_header(), self.progress, self._get_log_panel()))
            except:
                pass

    def _get_log_panel(self):
        """Create a panel with recent logs"""
        if not self.log_buffer:
            return Panel("", title="[dim]Activity Log[/]", border_style="dim")

        log_text = "\n".join(list(self.log_buffer))
        panel_height = min(len(self.log_buffer) + 2, 22)
        return Panel(log_text, title="[dim]Activity Log[/]", height=panel_height, border_style="dim")

    def _get_status_header(self):
        """Create status header showing real-time count"""
        from rich.text import Text

        status = Text()
        status.append("LinkedIn Leads Discovery", style="bold cyan")
        status.append("  •  ", style="dim")
        status.append("Discovering...", style="bold white")
        status.append("  •  ", style="dim")
        status.append(f"{len(self.discovered_profiles)} leads discovered", style="bold cyan")

        return Panel(status, border_style="cyan", padding=(0, 2))

    async def _add_discovered_profile(self, profile_data: Dict):
        """Thread-safe method to add profile and update display in real-time"""
        async with self.profile_lock:
            self.discovered_profiles.append(profile_data)
            # Update display immediately
            if self.live_display and self.progress:
                try:
                    self.live_display.update(Group(self._get_status_header(), self.progress, self._get_log_panel()))
                except:
                    pass

    async def discover_from_usernames(
        self,
        usernames: List[str],
        depth: int,
        api: AsyncLinkdAPI
    ) -> Dict:
        """
        Start discovery from a list of usernames
        Returns: dict with discovered profiles and stats
        """
        self.log_buffer.clear()
        self._add_log(f"[cyan]→ Starting discovery with {len(usernames)} usernames at depth {depth}[/]")

        # Set up API client callback
        self.api_client.log_callback = self._add_log

        # Create progress bar with percentage
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%")
        )
        task = progress.add_task(
            "[cyan]Discovering profiles...",
            total=depth
        )

        # Start Live display
        try:
            with Live(
                Group(self._get_status_header(), progress, self._get_log_panel()),
                console=console,
                refresh_per_second=10
            ) as live:
                self.live_display = live
                self.progress = progress

                starting_urns = []
                for username in usernames:
                    success, urn, error = await self.api_client.get_profile_urn(api, username)

                    if success and urn:
                        if urn not in self.seen_urns:
                            self.seen_urns.add(urn)
                            # Create starting profile with minimal data
                            # (full data will be fetched if we run similar on them)
                            starting_urns.append({
                                'urn': urn,
                                'id': '',
                                'publicIdentifier': username,
                                'firstName': '',
                                'lastName': '',
                                'headline': '',
                                'creator': False,
                                'profilePictureURL': '',
                                'username': username,
                                'depth': 0,
                                'source_urn': ''
                            })
                            self._add_log(f"[green]✓ {username} -> URN found[/]")
                        else:
                            self._add_log(f"[yellow]⊘ {username} -> Already discovered[/]")
                    else:
                        self.failed_usernames.append(username)
                        self._add_log(f"[red]✗ {username} -> {error}[/]")

                if not starting_urns:
                    self._add_log("[red]No valid URNs found from provided usernames[/]")
                    self.live_display = None
                    self.progress = None
                    return self._build_result()

                self._add_log(f"[green]Found {len(starting_urns)} starting profiles[/]")

                await self._discover_tree_iterative(starting_urns, depth, api, progress, task)

                self.live_display = None
                self.progress = None

        except KeyboardInterrupt:
            # Clean up display
            self.live_display = None
            self.progress = None
            self._add_log("[yellow]⚠ Discovery interrupted by user[/]")
            raise  # Re-raise to be caught by main

        return self._build_result()

    async def _discover_tree_iterative(
        self,
        starting_profiles: List[Dict],
        max_depth: int,
        api: AsyncLinkdAPI,
        progress: Progress,
        task_id
    ):
        """Iteratively discover profiles using queue (no recursion)"""
        # Queue stores tuples of (profile_info, depth_level)
        queue = [(profile, 0) for profile in starting_profiles]
        current_depth_level = 0

        while queue:
            # Get all profiles at current depth level
            current_batch = []
            remaining = []

            for profile_info, depth_level in queue:
                if depth_level == current_depth_level:
                    current_batch.append(profile_info)
                else:
                    remaining.append((profile_info, depth_level))

            queue = remaining

            if not current_batch:
                current_depth_level += 1
                continue

            # Save all profiles in current batch (only for starting profiles at depth 0)
            if current_depth_level == 0:
                for profile_info in current_batch:
                    if 'urn' in profile_info:
                        profile_data = profile_info.copy()
                        profile_data['depth_level'] = profile_info.get('depth', 0)
                        if 'depth' in profile_data:
                            del profile_data['depth']
                        await self._add_discovered_profile(profile_data)

            # Update progress
            progress.update(
                task_id,
                completed=current_depth_level
            )
            if self.live_display:
                self.live_display.update(Group(self._get_status_header(), progress, self._get_log_panel()))

            # Stop if we've reached max depth
            if current_depth_level >= max_depth:
                break

            self._add_log(f"[cyan]→ Processing depth level {current_depth_level + 1}/{max_depth}[/]")

            # Process all profiles in current batch concurrently
            semaphore = asyncio.Semaphore(self.max_concurrent)

            async def process_profile(profile_info: Dict):
                async with semaphore:
                    urn = profile_info['urn']
                    current_depth_val = profile_info.get('depth', 0)

                    success, similar_profiles, error = await self.api_client.get_similar_profiles(api, urn)

                    if success:
                        new_profiles = []
                        for similar in similar_profiles:
                            similar_urn = similar.get('urn')
                            if similar_urn and similar_urn not in self.seen_urns:
                                self.seen_urns.add(similar_urn)
                                profile_data = {
                                    'urn': similar_urn,
                                    'id': similar.get('id', ''),
                                    'publicIdentifier': similar.get('publicIdentifier', ''),
                                    'firstName': similar.get('firstName', ''),
                                    'lastName': similar.get('lastName', ''),
                                    'headline': similar.get('headline', ''),
                                    'creator': similar.get('creator', False),
                                    'profilePictureURL': similar.get('profilePictureURL', ''),
                                    'depth': current_depth_val + 1,
                                    'source_urn': urn
                                }
                                # Add to discovered profiles immediately for real-time counter update
                                profile_to_save = profile_data.copy()
                                profile_to_save['depth_level'] = profile_data['depth']
                                del profile_to_save['depth']
                                await self._add_discovered_profile(profile_to_save)

                                new_profiles.append(profile_data)

                        if new_profiles:
                            self._add_log(f"[green]✓ {urn[:20]}... -> Found {len(new_profiles)} new similar profiles[/]")
                        else:
                            self._add_log(f"[yellow]⊘ {urn[:20]}... -> No new profiles (all seen before)[/]")

                        return new_profiles
                    else:
                        self.failed_urns.append(urn)
                        self._add_log(f"[red]✗ {urn[:20]}... -> {error}[/]")
                        return []

            tasks = [process_profile(profile_info) for profile_info in current_batch]

            try:
                results = await asyncio.gather(*tasks)
            except (KeyboardInterrupt, asyncio.CancelledError):
                # Stop processing if interrupted
                self._add_log("[yellow]⚠ Discovery interrupted during batch processing[/]")
                raise KeyboardInterrupt  # Re-raise as KeyboardInterrupt for consistency

            # Add new profiles to queue
            for result in results:
                for profile in result:
                    queue.append((profile, profile['depth']))

            # Update progress
            progress.update(
                task_id,
                completed=current_depth_level + 1
            )
            if self.live_display:
                self.live_display.update(Group(self._get_status_header(), progress, self._get_log_panel()))

            self._add_log(f"[cyan]✓ Depth {current_depth_level + 1} complete: Found {len([p for p in results for _ in p])} new profiles[/]")
            self._add_log(f"[cyan]  Total discovered: {len(self.discovered_profiles)}[/]")

            current_depth_level += 1

    def _build_result(self) -> Dict:
        """Build final result dictionary"""
        return {
            'profiles': self.discovered_profiles,
            'total_discovered': len(self.discovered_profiles),
            'unique_urns': len(self.seen_urns),
            'failed_usernames': self.failed_usernames,
            'failed_urns': self.failed_urns,
            'activity_log': list(self.log_buffer)
        }

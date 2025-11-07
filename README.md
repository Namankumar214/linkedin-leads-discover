# LinkedIn Lead Scraper - Automated Profile Discovery & Lead Generation Tool

A powerful **LinkedIn scraper** and **lead discovery tool** that automatically finds and extracts similar LinkedIn profiles using tree-based exploration. This **LinkedIn automation tool** helps you discover hundreds or thousands of qualified leads by exploring professional networks - perfect for **LinkedIn prospecting**, sales, and recruitment.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

<video className="center" src="https://github-production-user-asset-6210df.s3.amazonaws.com/193476718/511409806-b3433ec1-c898-439f-9502-6420d7d7d8ea.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251107T160344Z&X-Amz-Expires=300&X-Amz-Signature=c0b70e3e34f47c72f4dc0372210ed9894e6f87f842bc311d062b213bba521316&X-Amz-SignedHeaders=host"></video>


## What Does This LinkedIn Lead Scraper Do?

This **LinkedIn profile finder** and **lead generation tool** automates the process of discovering potential leads by:

1. **Profile Discovery**: Starting with LinkedIn usernames you provide
2. **Network Exploration**: Finding similar profiles for each profile using LinkedIn's recommendation algorithm
3. **Deep Scraping**: Recursively discovering similar profiles of similar profiles (tree-based discovery)
4. **Smart Deduplication**: Automatically removing duplicate profiles across the discovery tree
5. **Data Export**: Exporting all discovered LinkedIn profiles to CSV or JSON format

**Real-World Example:** Start with 5 target profiles → Automatically discover 100-50,000+ similar leads in minutes!

### LinkedIn Scraper Features

✅ **Tree-Based LinkedIn Discovery** - Explores professional networks depth-first
✅ **Automated Lead Generation** - No manual LinkedIn searching required
✅ **Profile Data Extraction** - Scrapes names, headlines, profile URLs, and more
✅ **Real-Time Counter** - See leads discovered as they're found
✅ **Concurrent Processing** - Fast parallel profile scraping
✅ **Smart Deduplication** - Prevents duplicate profile extraction
✅ **Tree View Visualization** - See the complete discovery tree structure
✅ **Export to CSV/JSON/Tree** - Easy integration with CRM and sales tools 

---

## Quick Start - LinkedIn Lead Scraper Setup (3 Simple Steps)

### Step 1: Get Your LinkdAPI Key
1. Visit [linkdapi.com](https://linkdapi.com?p=signup) - the best **LinkedIn API** for profile data
2. Sign up for a free account
3. Copy your API key from the dashboard

### Step 2: Install LinkedIn Scraper
```bash
# Clone or download the project
cd linkedin-leads-discover

# Install Python dependencies
pip install -r requirements.txt

# OR use Python 3
pip3 install -r requirements.txt
```

### Step 3: Configure Your LinkedIn API Key
Open `config.ini` in any text editor and add your LinkdAPI key:
```ini
[LINKDAPI]
api_key = YOUR_API_KEY_HERE
```

### Step 4: Run the LinkedIn Lead Discovery Tool
```bash
python main.py
# OR
python3 main.py
```

---

## How to Use This LinkedIn Profile Scraper

### Starting the LinkedIn Lead Discovery Tool
Run `python main.py` and you'll see an interactive menu:

```
Choose action:
❯ Start discovery from usernames
  Start discovery from file
  View discovered profiles
  View tree
  Export profiles
  Exit
```

### Option 1: LinkedIn Scraper from Usernames
1. Select "Start discovery from usernames"
2. Enter LinkedIn usernames separated by commas:
   ```
   billgates, satyanadella, reidhoffman
   ```
3. Choose **discovery depth** (recommended: 3)
4. Watch the **LinkedIn lead scraper** work in real-time!

**How to find LinkedIn usernames:**
- From `linkedin.com/in/billgates` → use `billgates`
- From `linkedin.com/in/satya-nadella-3145136` → use `satya-nadella-3145136`
- The username is everything after `/in/` in the LinkedIn profile URL

### Option 2: Bulk LinkedIn Scraping from File
1. Create a text file with LinkedIn usernames (one per line):
   ```
   billgates
   satyanadella
   jeffweiner08
   reidhoffman
   ```
2. Select "Start discovery from file"
3. Enter the file path (default: `usernames.txt`)
4. Choose discovery depth
5. Let the **LinkedIn profile scraper** extract leads automatically!

### Option 3: View Discovery Tree
After running a discovery, select "View tree" to see the complete hierarchical structure of all discovered profiles:

```
LinkedIn Discovery Tree (3595 total profiles)
├── satyanadella │  (20 discovered)
│   ├── Aravind Srinivas │ Cofounder, President & CEO, Perplexity (19 discovered)
│   │   ├── Chungin Lee │ CEO @ Cluely, The AI notetaker that help... (16 discovered)
│   │   │   ├── Kevin  Lu │ Co-Founder @ Orchids (YC W25) | Prev @ P...
│   │   │   ├── Sajjaad Farzad │ Founding Engineer @ Cluely | Perusing Ba...
│   │   │   ├── Neel Shanmugam │ Co-Founder & COO @ Cluely | Z-Fellow | C...
│   │   │   ├── Fardeen Khimani 😇 │ CEO @ Rounds.so | Georgia Tech PhD Dropo...
│   │   │   ├── jonathan liu │ building Cupidly.io | boostrapping my wa...
│   │   │   └── ... and 11 more profiles
│   │   ├── Michael Yan │ Founder & CEO @ Simplify | Looking for a... (11 discovered)
│   │   │   ├── Sherry X. │ Partnerships & Strategy @ Simplify
│   │   │   ├── G Le │ Co-Founder @BuyAI | CS + Math @UIC | 1871
│   │   │   ├── Ethan Horoschak │ Founder @ Simplify | Hiring Senior SWEs!
│   │   │   ├── Nader Khalil │ Director @ NVIDIA | CEO & Co-founder at ...
│   │   │   ├── Mathis Grosjean │ Co-founder & CEO @ zealy.io
│   │   │   └── ... and 6 more profiles
│   │   ├── Arnav Gudibande │ Research Engineer @ Perplexity AI (11 discovered)
│   │   │   ├── Patrick Liu │ AI @ Perplexity | BS/MS CS @ Stanford
│   │   │   ├── Larry Yang │ ‎Software Engineer
│   │   │   ├── William Wong │ Research Engineer at DeepMind
│   │   │   ├── Alexis Weill │ Data Science at Perplexity
│   │   │   ├── Clare Southern │ Perplexity AI
│   │   │   └── ... and 6 more profiles
│   │   └── ... and 14 more profiles
│   ├── N. Chandrasekaran │ Chairman, Tata Sons, Author of Bridgital... (9 discovered)
│   │   ├── Kunal Shah │ Founder : CRED, curious.  (1 discovered)
│   │   │   └── Nithin Kamath │ Founder & CEO at Zerodha & Rainmatter. L...
│   │   ├── Arundhati Bhattacharya │ President & CEO at Salesforce, South Asia (9 discovered)
│   │   │   ├── Arun Kumar Parameswaran │ Executive Vice President & Managing Dire...
│   │   │   ├── Niraj Ambani │ Group President - Supply Chain at Relian...
│   │   │   └── ... and 4 more profiles
│   │   └── ... and 4 more profiles
│   ├── Andrew Ng │ Founder of DeepLearning.AI; Managing Gen... (15 discovered)
│   │   ├── Lilian Weng │ AI Researcher, Co-founder @ Thinking Mac... (14 discovered)
│   │   │   ├── Rowan Zellers │ thinking machines, ex-openai
│   │   │   ├── Jonathan Lachman │ Founding Head of Operations at Thinking ...
│   │   │   └── ... and 9 more profiles
│   │   └── ... and 10 more profiles
│   └── ... and 15 more profiles
└── jeffweiner08 │  (19 discovered)
    ├── Laszlo Bock │ 2x start-up founder & CEO --​> 2 exits |... (19 discovered)
    │   ├── Kevin Oakes │ Founder & Chief Strategy Officer of the ... (6 discovered)
    │   │   ├── Betsy Rodriguez, PhD │ Retired Chief HR Officer
    │   │   ├── Alexis Fink │ AI Activation | Future of Work | Leaders...
    │   │   └── ... and 1 more profiles
    │   ├── Jon Ingham │ Director of the Strategic HR Academy. Ex... (12 discovered)
    │   │   ├── Albert Loyola │ Human-AI Workforce Advisor | Workforce S...
    │   │   ├── William Tincup │ I say what others don't, can't, or won't.
    │   │   └── ... and 7 more profiles
    │   └── ... and 14 more profiles
    └── ... and 15 more profiles
```

The tree view shows:
- **Visual hierarchy** of how profiles were discovered
- **Connection paths** from seed profiles to discovered leads
- **Discovery count** for each profile (how many profiles they led to)
- **Profile details** including name and headline
- **Collapsed view** for large branches (e.g., "... and 11 more profiles")

### Understanding Discovery Depth - LinkedIn Lead Mining

**Depth** controls how deep the LinkedIn network exploration goes:

- **Depth 1**: Only your seed/starting profiles
- **Depth 2**: Starting profiles + their LinkedIn similar profiles (~20 per profile)
- **Depth 3**: Depth 2 + similar profiles of those (~400+ total profiles)
- **Depth 5**: Discovers thousands of LinkedIn leads
- **Depth 10**: Can discover tens of thousands of profiles!

**LinkedIn Lead Generation Growth Example (5 starting profiles):**
- Depth 1: 5 profiles
- Depth 2: ~105 profiles (5 + ~20 similar per profile)
- Depth 3: ~2,105 profiles (exponential growth)
- Depth 5: Can reach 40,000+ LinkedIn profiles!

**Note**: Higher depth = more profiles discovered = more API credits used

---

## LinkedIn Scraper Features & Capabilities

### 🌳 Tree-Based LinkedIn Network Discovery
Intelligently explores LinkedIn's "People Also Viewed" algorithm to discover similar profiles at each level of your professional network

### ♻️ Smart Deduplication - No Duplicate Leads
Automatically detects and skips duplicate LinkedIn profiles using URN tracking (same person found through multiple paths)

### ⚡ Fast & Concurrent LinkedIn Scraping
Processes multiple LinkedIn profiles simultaneously using async/await for maximum speed and efficiency

### 🎯 Intelligent Retry Logic
Automatically retries failed LinkedIn API requests with exponential backoff for rate limits

### 📊 Real-Time Lead Counter
Watch your **LinkedIn leads** counter increment in real-time as profiles are discovered (not just after each depth completes)

### 💾 Flexible Data Export
- **CSV Export**: Perfect for Excel, Google Sheets, CRM import, and data analysis
- **JSON Export**: Complete structured data for developers and automation
- **Tree Export**: Visual hierarchy showing discovery paths and relationships

### 🎨 Beautiful CLI Interface
Clean command-line interface with colors, progress bars, spinners, and easy arrow-key navigation

### 🌲 Tree View Visualization
View the complete discovery hierarchy showing:
- How each profile was discovered and their relationships
- Visual tree structure with branch connections
- Profile counts showing how many leads each person generated
- Collapsible branches for easy navigation of large networks

### 🔄 LinkedIn Profile Data Extraction
Each discovered profile includes:
- LinkedIn URN (unique identifier)
- Profile ID & Public Identifier (username)
- First Name & Last Name
- Professional Headline
- Profile Picture URL
- Creator Status
- Discovery Depth Level
- Source Profile (who they were discovered from)

---

## Configuration Options - LinkedIn Scraper Settings

Edit `config.ini` to customize your **LinkedIn lead scraper** behavior:

```ini
[LINKDAPI]
# Your API key from https://linkdapi.com
api_key = YOUR_API_KEY_HERE

[SETTINGS]
# How many LinkedIn profiles to scrape concurrently (1-50)
# Higher = faster lead discovery but uses more API credits
max_concurrent_requests = 10

# Where to save exported LinkedIn data
output_directory = output

# How many times to retry failed LinkedIn API requests
max_retries = 3

# Delay between retries (seconds)
retry_delay = 2

# Default depth for LinkedIn discovery (1-10)
default_depth = 3
```

### Recommended LinkedIn Scraping Settings by Plan

| LinkdAPI Plan | max_concurrent_requests | Recommended Depth | Leads Per Session |
|---------------|------------------------|-------------------|-------------------|
| Free Trial | 5 | 2-3 | 100-500 |
| Starter | 10 | 3-4 | 500-2,000 |
| Professional | 20 | 4-5 | 2,000-10,000 |
| Enterprise | 30-50 | 5-10 | 10,000-100,000+ |

---

## LinkedIn Data Export Formats

### CSV Export - LinkedIn Lead Lists
Perfect for Excel, Google Sheets, Salesforce, HubSpot, or any CRM:
- **URN**: Unique LinkedIn profile identifier
- **Profile ID**: LinkedIn numeric ID
- **Public Identifier**: LinkedIn username/vanity URL
- **First Name & Last Name**: Professional name
- **Headline**: Job title and professional summary
- **Profile Picture URL**: Avatar/headshot URL
- **Creator Status**: LinkedIn content creator badge
- **Depth Level**: Which discovery level they were found at
- **Source URN**: The profile that led to this discovery

### JSON Export - Structured LinkedIn Data
Complete nested data structure for:
- Custom integrations
- Data pipelines
- Advanced analytics
- CRM automation
- Lead scoring systems

### Tree Export - Visual Discovery Hierarchy
Beautiful text-based tree visualization showing:
- **Complete discovery path** from seed profiles to all discovered leads
- **Hierarchical structure** showing parent-child relationships
- **Profile counts** at each node (how many profiles each person led to)
- **Profile details** including names and headlines
- **Smart collapsing** for large branches (shows first 5, then "... and X more")
- Perfect for understanding network relationships and discovery patterns
- Can be saved to text file for documentation or sharing

---

## Real-World Use Cases - LinkedIn Lead Generation

### 🎯 Sales & B2B Lead Generation
**LinkedIn prospecting** made easy:
1. Find 5-10 profiles of your ideal customer/decision maker
2. Run the **LinkedIn lead scraper** with depth 4-5
3. Export discovered leads to CSV
4. Import to your CRM (Salesforce, HubSpot, Pipedrive, etc.)
5. Start outreach campaigns with hundreds of qualified leads

### 💼 Recruitment & Talent Sourcing
Build candidate pipelines with **LinkedIn profile discovery**:
1. Find profiles with specific job titles (e.g., "Senior React Developer")
2. Use the **LinkedIn scraper** to discover similar professionals
3. Export to CSV and filter by headline/skills
4. Reach out to top candidates for your open positions

### 📊 Market Research & Competitive Analysis
Analyze professional networks and industries:
1. Start with key industry players and competitors
2. Discover their LinkedIn network connections
3. Export for competitive intelligence analysis
4. Identify market trends and hiring patterns

### 🤝 Partnership & Business Development
Find potential partners and collaborators:
1. Identify successful companies, founders, and investors
2. Run **LinkedIn network discovery** to find similar profiles
3. Research and prioritize partnership opportunities
4. Build targeted outreach lists

### 💡 Content Marketing & Influencer Outreach
Discover LinkedIn influencers and content creators:
1. Start with known industry influencers
2. Use the scraper to find similar creators
3. Filter by creator status in exported data
4. Build influencer outreach campaigns

---

## LinkedIn Scraping Examples

### Example 1: Quick Lead Discovery - 100 Leads
```bash
# Run the LinkedIn lead scraper
python main.py

# Select: Start discovery from usernames
# Enter: billgates, satyanadella, jeffweiner08
# Depth: 2
# Result: ~65 new LinkedIn profiles discovered in 2-5 seconds
```

### Example 2: Deep Lead Mining - Thousands of Leads
```bash
# Create usernames.txt with 10 target LinkedIn profiles
# Run the tool
python main.py

# Select: Start discovery from file
# File: usernames.txt
# Depth: 5
# Result: 5,000-10,000+ LinkedIn profiles discovered!
```

### Example 3: Targeted Industry Lead Generation
```bash
# Manually find 5 CEOs/founders in your target industry on LinkedIn
# Add their usernames to a file (e.g., tech_ceos.txt)
# Run LinkedIn discovery with depth 4-5
# Export to CSV
# Result: Hundreds of similar CEOs and decision makers!
```

### Example 4: Sales Prospecting Campaign
```bash
# Find 10 existing customers on LinkedIn
# Run discovery depth 3-4
# Export to CSV with ~2,000 similar profiles
# Import to CRM for cold outreach campaign
```

### Example 5: Understanding Network Relationships
```bash
# Run LinkedIn discovery with depth 3-4
# Select "View tree" to visualize the discovery hierarchy
# See how profiles are connected and who led to which discoveries
# Export tree to text file for team sharing or documentation
# Use insights to understand network patterns and target key connectors
```

---

## Tips & Best Practices - LinkedIn Lead Scraping

### 🎯 Start Small and Test Your LinkedIn Scraper
- Begin with depth 2-3 to test the quality of discovered leads
- Review the exported LinkedIn profiles
- Adjust your seed profiles if needed
- Increase depth once you're satisfied with results

### 💰 Manage LinkdAPI Credits Efficiently
- Monitor your API usage at [linkdapi.com/dash](https://linkdapi.com/dash)
- Each LinkedIn profile scraped = 1 API call
- Depth 5 with 10 starting profiles ≈ 10,000 API calls
- Use lower depth for testing, higher depth for production scraping

### 🎨 Choose Quality Seed Profiles
- Pick LinkedIn profiles that represent your ideal customer/candidate
- The algorithm finds profiles similar to your seeds
- Better seed profiles = higher quality discovered leads
- Use profiles with complete LinkedIn data for best results

### 📊 Export LinkedIn Data Regularly
- Export after each discovery session to prevent data loss
- Don't run multiple discoveries without exporting
- Use timestamped filenames to organize lead lists
- Back up exported CSV/JSON files regularly

### ⚡ Optimize LinkedIn Scraping Speed
- Increase `max_concurrent_requests` if you have a paid LinkdAPI plan
- Lower depth = faster discovery but fewer leads
- Split large scraping jobs into batches
- Use file input for bulk LinkedIn profile discovery

### 🔍 Filter and Qualify Leads Post-Scraping
- Use Excel/Sheets to filter by headline, name patterns
- Remove profiles outside your target geography
- Score leads based on job titles and company size
- Prioritize by discovery depth (lower depth = closer match)

### 🌲 Leverage Tree View for Network Insights
- View tree after discovery to understand network relationships
- Identify key connectors who led to many high-quality leads
- Use discovery paths to personalize outreach ("found through X")
- Export tree visualization for team sharing and documentation
- Analyze which seed profiles generated the best lead quality

---

## Troubleshooting LinkedIn Scraper Issues

### "Config file not found"
**Solution**: Ensure `config.ini` exists in the same folder as `main.py`

### "Please set your LinkdAPI key"
**Solution**:
1. Open `config.ini` in a text editor
2. Replace `YOUR_API_KEY_HERE` with your actual API key from [linkdapi.com](https://linkdapi.com)
3. Save the file and restart the scraper

### "No module named 'linkdapi'"
**Solution**: Install required dependencies
```bash
pip install -r requirements.txt
# OR
pip3 install -r requirements.txt
```

### "Rate limit exceeded" - LinkedIn API Limits
**Solution**:
- The tool automatically retries with exponential backoff
- If it happens frequently, reduce `max_concurrent_requests` in config.ini
- Check your LinkdAPI plan limits at [linkdapi.com/dash](https://linkdapi.com/dash)
- Upgrade to a higher plan for more concurrent scraping

### "No LinkedIn profiles discovered"
**Possible causes**:
- LinkedIn usernames are incorrect (check spelling and format)
- Profiles don't exist or are private
- LinkdAPI key is invalid or expired
- No API credits remaining on your account

### LinkedIn Scraper Running Slowly
**Solutions**:
1. Increase `max_concurrent_requests` in config.ini (if your plan allows)
2. Reduce discovery depth for faster scraping
3. Check your internet connection speed
4. Verify LinkdAPI service status

### Real-Time Counter Not Updating
**Solution**: This has been fixed! Leads now increment immediately as they're discovered (not after each depth level completes)

---

## Advanced LinkedIn Scraping Techniques

### Combining Multiple Seed Lists
1. Create separate files for different lead segments (competitors, customers, prospects)
2. Run discoveries separately for each segment
3. Combine exported CSV files in Excel/Sheets
4. Remove duplicates using LinkedIn URN as unique key

### Lead Scoring with LinkedIn Data
Export to CSV and add scoring columns:
- **Title Match Score**: How closely headline matches target job title
- **Seniority Score**: C-level (10), VP (8), Director (6), Manager (4)
- **Discovery Depth**: Lower depth = higher relevance score
- **Company Size**: Based on company in headline
- **Geography**: Based on location (if available)

### Integrating with CRM Systems
1. Export LinkedIn leads to CSV
2. Map CSV columns to CRM fields:
   - First Name → First Name
   - Last Name → Last Name
   - Headline → Job Title
   - Public Identifier → LinkedIn URL (concat with linkedin.com/in/)
   - Profile Picture URL → Avatar
3. Import using CRM's CSV import feature
4. Create automated workflows for lead nurturing

### Building Custom LinkedIn Sales Funnels
1. **Top of Funnel**: Scrape broad profiles (depth 5-6, generic seeds)
2. **Middle of Funnel**: Scrape targeted profiles (depth 3-4, specific seeds)
3. **Bottom of Funnel**: Scrape high-intent profiles (depth 2, ideal customer seeds)
4. Prioritize outreach by funnel stage

---

## LinkedIn Scraper Performance & Scalability

### Speed Benchmarks
- **Concurrent Requests: 10, Depth 3**: ~500 profiles in 5-10 seconds
- **Concurrent Requests: 20, Depth 4**: ~2,000 profiles in 15-25 seconds
- **Concurrent Requests: 30, Depth 5**: ~10,000 profiles in 30-60 seconds
- **Concurrent Requests: 50, Depth 6**: ~50,000 profiles in 2-4 minutes

*Actual speed depends on LinkdAPI plan, network speed, and API response times*

### Scalability Considerations
- **Memory Usage**: Minimal, profiles stored in-memory as list
- **Disk Space**: CSV exports are typically 100KB-10MB depending on volume
- **API Limits**: Respects LinkdAPI rate limits with automatic retries
- **Deduplication**: O(1) lookup using Set data structure, no performance degradation

---

## LinkedIn API & Legal Compliance

### Using LinkdAPI - The Best LinkedIn API
This **LinkedIn scraper** uses [LinkdAPI](https://linkdapi.com), a reliable LinkedIn data API that:
- Provides access to public LinkedIn profile data
- Handles authentication and rate limiting
- Offers affordable pricing with free trial
- Includes profile overview, similar profiles, search, and more endpoints

### Legal & Ethical Use
This **LinkedIn lead generation tool** is for educational, research, and legitimate business purposes only.

**Users are responsible for:**
- ✅ Complying with LinkedIn's Terms of Service
- ✅ Respecting data privacy laws (GDPR, CCPA, etc.)
- ✅ Using scraped data ethically and legally
- ✅ Obtaining consent before marketing/outreach
- ✅ Following CAN-SPAM, CASL, and anti-spam regulations
- ❌ NOT using data for spam or harassment
- ❌ NOT violating intellectual property rights
- ❌ NOT discriminating based on protected characteristics

**The LinkdAPI Team and tool creators are not responsible for misuse.**

### GDPR & Privacy Compliance
When using this LinkedIn scraper:
- Only scrape public profile data
- Provide opt-out mechanisms in outreach
- Store data securely
- Delete data when no longer needed
- Document your legal basis for processing
- Include privacy notices in communications

---

## Output Files - Exported LinkedIn Data

All LinkedIn lead exports are saved to the `output/` folder with timestamps:

```
output/
  linkedin_leads_20250106_143022.csv    # CSV format for CRM import
  linkedin_leads_20250106_150135.json   # JSON format for developers
  linkedin_tree_20250106_150135.txt     # Tree visualization format
```

**File Naming Convention**:
- CSV/JSON: `linkedin_leads_YYYYMMDD_HHMMSS.extension`
- Tree: `linkedin_tree_YYYYMMDD_HHMMSS.txt`

---

## FAQs - LinkedIn Lead Scraper

**Q: How many LinkedIn profiles can I scrape?**
A: Depends on your discovery depth and seed profiles. With depth 5 and 10 seeds, you can discover 5,000-50,000+ profiles!

**Q: Does this LinkedIn scraper cost money?**
A: LinkdAPI has a free trial with limited credits. After that, you pay per API call. Each profile discovered = 1 API call. Check pricing at [https://linkdapi.com/#pricing](https://linkdapi.com/#pricing)

**Q: Will I get duplicate LinkedIn profiles?**
A: No! The tool uses intelligent deduplication with URN tracking to prevent duplicates across the entire discovery tree.

**Q: How long does LinkedIn scraping take?**
A: Depends on depth and concurrent requests:
- Depth 2: 1-5 minutes
- Depth 3: 5-15 minutes
- Depth 5: 15-60 minutes
- Depth 7+: 1-4 hours

**Q: Is this LinkedIn scraper legal?**
A: This tool uses LinkdAPI's official LinkedIn API for public profile data. Always follow LinkedIn's ToS and respect privacy laws.

**Q: Can I pause and resume LinkedIn scraping?**
A: Currently no, but you can export results and start a new discovery session later with different seeds.

**Q: What's the difference between this and LinkedIn Sales Navigator?**
A: LinkedIn Sales Navigator is LinkedIn's official paid tool for B2B sales. This open-source scraper uses the LinkdAPI to automate profile discovery at a lower cost with more flexibility and data export options.

**Q: Can I scrape LinkedIn company pages?**
A: This tool focuses on LinkedIn profile/people discovery. For company data, check out other LinkdAPI endpoints.

**Q: Does this work with LinkedIn Recruiter accounts?**
A: This tool doesn't require any LinkedIn account. It uses the LinkdAPI to access public profile data.

**Q: Can I discover people in specific locations or industries?**
A: The tool discovers profiles similar to your seeds. To target specific locations/industries, choose seed profiles from those segments.

**Q: How accurate is the "similar profiles" algorithm?**
A: It uses LinkedIn's own recommendation engine (People Also Viewed). Accuracy depends on the quality of your seed profiles and how complete the LinkedIn profiles are.

**Q: What is the tree view and how do I use it?**
A: The tree view shows a visual hierarchy of all discovered profiles, displaying how each profile led to other discoveries. After running a discovery session, select "View tree" from the menu to see the complete network structure. You can also export the tree to a text file for documentation or sharing with your team.

**Q: Can I export the tree visualization?**
A: Yes! When viewing the tree or exporting profiles, select the tree export format. It will save a beautifully formatted text file showing the complete discovery hierarchy with all relationships and profile details.

---

## Support & Resources

### Need Help with LinkedIn Scraping?
- 📧 Email: support@linkdapi.com
- 🌐 Website: [linkdapi.com](https://linkdapi.com)
- 📚 API Documentation: [linkdapi.com/docs](https://linkdapi.com/docs)
- 💬 Community Support: Check our GitHub issues

### Report LinkedIn Scraper Issues
- Create an issue on GitHub with:
  - Error messages and stack traces
  - Steps to reproduce the problem
  - Your Python version and OS
  - Anonymized config.ini (remove API key)

### Get Your LinkdAPI Key - Best LinkedIn API
- 🔑 Sign up at [linkdapi.com](https://linkdapi.com/?p=signup)
- ✨ Free trial with credits included
- 📊 Affordable pricing for all business sizes
- ⚡ Fast and reliable LinkedIn data API

---

## Technical Stack - LinkedIn Scraper Architecture

**Language**: Python 3.8+
**LinkedIn API**: LinkdAPI (Async)
**CLI Framework**: Rich (beautiful terminal UI)
**Input Handling**: Questionary (arrow-key menus)
**Async Processing**: asyncio + asyncio.gather
**Data Export**: CSV (built-in) + JSON (built-in)
**Configuration**: ConfigParser (.ini files)

**Architecture Pattern**: Tree-based iterative discovery with concurrent processing and smart deduplication using URN Sets

---

## Contributing to LinkedIn Scraper

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Open GitHub issues with details
2. **Suggest Features**: Share ideas for new LinkedIn scraping capabilities
3. **Submit PRs**: Follow Python best practices (PEP 8, type hints, docstrings)
4. **Improve Docs**: Help make this README even better
5. **Share Use Cases**: Tell us how you're using the LinkedIn lead scraper

---

## Disclaimer - LinkedIn Scraping

This **LinkedIn lead generation tool** and **LinkedIn profile scraper** is provided for:
- ✅ Educational purposes
- ✅ Research and analysis
- ✅ Legitimate business use (sales, recruitment, marketing)

**Users are solely responsible for:**
- Complying with all applicable laws and regulations
- Following LinkedIn's Terms of Service
- Respecting data privacy and protection laws (GDPR, CCPA, etc.)
- Using scraped data ethically and legally
- Obtaining necessary consents for marketing/outreach

**The creators, LinkdAPI Team, and contributors are not liable for:**
- Misuse of this LinkedIn scraping tool
- Violations of LinkedIn's Terms of Service
- Privacy law violations
- Damages resulting from use of this software

**Use responsibly and ethically. Respect people's privacy and professional boundaries.**

---

**💙 Built with [LinkdAPI](https://linkdapi.com) - The Best LinkedIn API**

*Questions about LinkedIn scraping or lead generation? Email us at support@linkdapi.com*

---

**⭐ Star this repo if you find this LinkedIn lead scraper useful!**

**🔗 Share with your sales, marketing, and recruitment teams!**

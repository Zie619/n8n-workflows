# ⚡ N8N Workflow Collection & Documentation

A professionally organized collection of **2,057 n8n workflows** with a lightning-fast documentation system that provides instant search, analysis, and browsing capabilities.

> **⚠️ IMPORTANT NOTICE (Aug 14, 2025):** Repository history has been rewritten due to DMCA compliance. If you have a fork or local clone, please see [Issue 85](https://github.com/Zie619/n8n-workflows/issues/85) for instructions on syncing your copy.
> 
## Support My Work

[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black&style=flat)](https://www.buymeacoffee.com/zie619)

If you'd like to say thanks, consider buying me a coffee—your support helps me keep improving this project!

## 🚀 **NEW: Public Search Interface & High-Performance Documentation**

**🌐 [Browse workflows online](https://zie619.github.io/n8n-workflows) - No installation required!**

**Or run locally for development with 100x performance improvement:**

### Option 1: Online Search (Recommended for Users)
**🔗 Visit: [zie619.github.io/n8n-workflows](https://zie619.github.io/n8n-workflows)**
- ⚡ **Instant access** - No setup required
- 🔍 **Search 2,057+ workflows** directly in browser
- 📱 **Mobile-friendly** interface
- 🏷️ **Category filtering** across 15 categories
- 📥 **Direct download** of workflow JSON files

### Option 2: Local Development System
```bash
# Install dependencies
pip install -r requirements.txt

# Start the fast API server
python run.py

# Open in browser
http://localhost:8000
```

**Features:**
- ⚡ **Sub-100ms response times** with SQLite FTS5 search
- 🔍 **Instant full-text search** with advanced filtering
- 📱 **Responsive design** - works perfectly on mobile
- 🌙 **Dark/light themes** with system preference detection
- 📊 **Live statistics** - 365 unique integrations, 29,445 total nodes
- 🎯 **Smart categorization** by trigger type and complexity
- 🎯 **Use case categorization** by service name mapped to categories
- 📄 **On-demand JSON viewing** and download
- 🔗 **Mermaid diagram generation** for workflow visualization
- 🔄 **Real-time workflow naming** with intelligent formatting

### Performance Comparison

| Metric | Old System | New System | Improvement |
|--------|------------|------------|-------------|
| **File Size** | 71MB HTML | <100KB | **700x smaller** |
| **Load Time** | 10+ seconds | <1 second | **10x faster** |
| **Search** | Client-side only | Full-text with FTS5 | **Instant** |
| **Memory Usage** | ~2GB RAM | <50MB RAM | **40x less** |
| **Mobile Support** | Poor | Excellent | **Fully responsive** |

---

## 📂 Repository Organization

### Workflow Collection
- **2,057 workflows** with meaningful, searchable names
- **365 unique integrations** across popular platforms
- **29,445 total nodes** with professional categorization
- **Quality assurance** - All workflows analyzed and categorized

### Advanced Naming System ✨
Our intelligent naming system converts technical filenames into readable titles:
- **Before**: `2051_Telegram_Webhook_Automation_Webhook.json`
- **After**: `Telegram Webhook Automation`
- **100% meaningful names** with smart capitalization
- **Automatic integration detection** from node analysis

### Use Case Category ✨

The search interface includes a dropdown filter that lets you browse 2,057+ workflows by category.

The system includes an automated categorization feature that organizes workflows by service categories to make them easier to discover and filter.

### How Categorization Works

1. **Run the categorization script**
   ```
   python create_categories.py
   ```

2. **Service Name Recognition**
   The script analyzes each workflow JSON filename to identify recognized service names (e.g., "Twilio", "Slack", "Gmail", etc.)

3. **Category Mapping**
   Each recognized service name is matched to its corresponding category using the definitions in `context/def_categories.json`. For example:
   - Twilio → Communication & Messaging
   - Gmail → Communication & Messaging  
   - Airtable → Data Processing & Analysis
   - Salesforce → CRM & Sales

4. **Search Categories Generation**
   The script produces a `search_categories.json` file that contains the categorized workflow data

5. **Filter Interface**
   Users can then filter workflows by category in the search interface, making it easier to find workflows for specific use cases

### Available Categories

The categorization system includes the following main categories:
- AI Agent Development
- Business Process Automation
- Cloud Storage & File Management
- Communication & Messaging
- Creative Content & Video Automation
- Creative Design Automation
- CRM & Sales
- Data Processing & Analysis
- E-commerce & Retail
- Financial & Accounting
- Marketing & Advertising Automation
- Project Management
- Social Media Management
- Technical Infrastructure & DevOps
- Web Scraping & Data Extraction

### Contribute Categories

You can help expand the categorization by adding more service-to-category mappings (e.g., Twilio → Communication & Messaging) in context/defs_categories.json.

Many workflow JSON files are conveniently named with the service name, often separated by underscores (_).


---

## 🛠 Usage Instructions

### Option 1: Modern Fast System (Recommended)
```bash
# Clone repository
git clone <repo-url>
cd n8n-workflows

# Install Python dependencies
pip install -r requirements.txt

# Start the documentation server
python run.py

# Browse workflows at http://localhost:8000
# - Instant search across 2,057 workflows
# - Professional responsive interface
# - Real-time workflow statistics
```

### Option 2: Development Mode
```bash
# Start with auto-reload for development
python run.py --dev

# Or specify custom host/port
python run.py --host 0.0.0.0 --port 3000

# Force database reindexing
python run.py --reindex
```

### Import Workflows into n8n
```bash
# Use the Python importer (recommended)
python import_workflows.py

# Or manually import individual workflows:
# 1. Open your n8n Editor UI
# 2. Click menu (☰) → Import workflow
# 3. Choose any .json file from the workflows/ folder
# 4. Update credentials/webhook URLs before running
```

---

## 📊 Workflow Statistics

### Current Collection Stats
- **Total Workflows**: 2,057 automation workflows
- **Active Workflows**: 215 (10.5% active rate)
- **Total Nodes**: 29,528 (avg 14.4 nodes per workflow)
- **Unique Integrations**: 367 different services and APIs
- **Database**: SQLite with FTS5 full-text search

### Trigger Distribution
- **Complex**: 832 workflows (40.4%) - Multi-trigger systems
- **Webhook**: 521 workflows (25.3%) - API-triggered automations  
- **Manual**: 478 workflows (23.2%) - User-initiated workflows
- **Scheduled**: 226 workflows (11.0%) - Time-based executions

### Complexity Analysis
- **Low (≤5 nodes)**: ~35% - Simple automations
- **Medium (6-15 nodes)**: ~45% - Standard workflows
- **High (16+ nodes)**: ~20% - Complex enterprise systems

### Popular Integrations
Top services by usage frequency:
- **Communication**: Telegram, Discord, Slack, WhatsApp
- **Cloud Storage**: Google Drive, Google Sheets, Dropbox
- **Databases**: PostgreSQL, MySQL, MongoDB, Airtable
- **AI/ML**: OpenAI, Anthropic, Hugging Face
- **Development**: HTTP Request, Webhook, GraphQL

---

## 🔍 Advanced Search Features

### Smart Search Categories
Our system automatically categorizes workflows into 15 main categories:

#### Available Categories:
- **AI Agent Development**: OpenAI, Anthropic, Hugging Face, CalcsLive
- **Business Process Automation**: Workflow utilities, scheduling, data processing
- **Cloud Storage & File Management**: Google Drive, Dropbox, OneDrive, Box
- **Communication & Messaging**: Telegram, Discord, Slack, WhatsApp, Email
- **Creative Content & Video Automation**: YouTube, Vimeo, content creation
- **Creative Design Automation**: Canva, Figma, image processing
- **CRM & Sales**: Salesforce, HubSpot, Pipedrive, customer management
- **Data Processing & Analysis**: Database operations, analytics, data transformation
- **E-commerce & Retail**: Shopify, Stripe, PayPal, online stores
- **Financial & Accounting**: Financial tools, payment processing, accounting
- **Marketing & Advertising Automation**: Email marketing, campaigns, lead generation
- **Project Management**: Jira, Trello, Asana, task management
- **Social Media Management**: LinkedIn, Twitter/X, Facebook, Instagram
- **Technical Infrastructure & DevOps**: GitHub, deployment, monitoring
- **Web Scraping & Data Extraction**: HTTP requests, webhooks, data collection

### API Usage Examples
```bash
# Search workflows by text
curl "http://localhost:8000/api/workflows?q=telegram+automation"

# Filter by trigger type and complexity
curl "http://localhost:8000/api/workflows?trigger=Webhook&complexity=high"

# Find all messaging workflows
curl "http://localhost:8000/api/workflows/category/messaging"

# Get database statistics
curl "http://localhost:8000/api/stats"

# Browse available categories
curl "http://localhost:8000/api/categories"
```

---

## 🏗 Technical Architecture

### Modern Stack
- **SQLite Database** - FTS5 full-text search with 365 indexed integrations
- **FastAPI Backend** - RESTful API with automatic OpenAPI documentation
- **Responsive Frontend** - Modern HTML5 with embedded CSS/JavaScript
- **Smart Analysis** - Automatic workflow categorization and naming

### Key Features
- **Change Detection** - MD5 hashing for efficient re-indexing
- **Background Processing** - Non-blocking workflow analysis
- **Compressed Responses** - Gzip middleware for optimal speed
- **Error Handling** - Graceful degradation and comprehensive logging
- **Mobile Optimization** - Touch-friendly interface design

### Database Performance
```sql
-- Optimized schema for lightning-fast queries
CREATE TABLE workflows (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE,
    name TEXT,
    active BOOLEAN,
    trigger_type TEXT,
    complexity TEXT,
    node_count INTEGER,
    integrations TEXT,  -- JSON array of 365 unique services
    description TEXT,
    file_hash TEXT,     -- MD5 for change detection
    analyzed_at TIMESTAMP
);

-- Full-text search with ranking
CREATE VIRTUAL TABLE workflows_fts USING fts5(
    filename, name, description, integrations, tags,
    content='workflows', content_rowid='id'
);
```

---

## 🔧 Setup & Requirements

### System Requirements
- **Python 3.7+** - For running the documentation system
- **Modern Browser** - Chrome, Firefox, Safari, Edge
- **50MB Storage** - For SQLite database and indexes
- **n8n Instance** - For importing and running workflows

### Installation
```bash
# Clone repository
git clone <repo-url>
cd n8n-workflows

# Install dependencies
pip install -r requirements.txt

# Start documentation server
python run.py

# Access at http://localhost:8000
```

### Development Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run with auto-reload for development
python api_server.py --reload

# Force database reindexing
python workflow_db.py --index --force
```

---

## 📋 Naming Convention

### Intelligent Formatting System
Our system automatically converts technical filenames to user-friendly names:

```bash
# Automatic transformations:
2051_Telegram_Webhook_Automation_Webhook.json → "Telegram Webhook Automation"
0250_HTTP_Discord_Import_Scheduled.json → "HTTP Discord Import Scheduled"  
0966_OpenAI_Data_Processing_Manual.json → "OpenAI Data Processing Manual"
```

### Technical Format
```
[ID]_[Service1]_[Service2]_[Purpose]_[Trigger].json
```

### Smart Capitalization Rules
- **HTTP** → HTTP (not Http)
- **API** → API (not Api)  
- **webhook** → Webhook
- **automation** → Automation
- **scheduled** → Scheduled

---

## 🚀 API Documentation

### Core Endpoints
- `GET /` - Main workflow browser interface
- `GET /api/stats` - Database statistics and metrics
- `GET /api/workflows` - Search with filters and pagination
- `GET /api/workflows/{filename}` - Detailed workflow information
- `GET /api/workflows/{filename}/download` - Download workflow JSON
- `GET /api/workflows/{filename}/diagram` - Generate Mermaid diagram

### Advanced Search
- `GET /api/workflows/category/{category}` - Search by service category
- `GET /api/categories` - List all available categories
- `GET /api/integrations` - Get integration statistics
- `POST /api/reindex` - Trigger background reindexing

### Response Examples
```json
// GET /api/stats
{
  "total": 2053,
  "active": 215,
  "inactive": 1838,
  "triggers": {
    "Complex": 831,
    "Webhook": 519,
    "Manual": 477,
    "Scheduled": 226
  },
  "total_nodes": 29445,
  "unique_integrations": 365
}
```

---

## 🤝 Contributing

**🎉 This project solves [Issue #84](https://github.com/Zie619/n8n-workflows/issues/84) - providing online access to workflows without requiring local setup!**

### Adding New Workflows
1. **Export workflow** as JSON from n8n
2. **Name descriptively** following the established pattern: `[ID]_[Service]_[Purpose]_[Trigger].json`
3. **Add to workflows/** directory (create service folder if needed)
4. **Remove sensitive data** (credentials, personal URLs)
5. **Add tags** for better searchability (calculation, automation, etc.)
6. **GitHub Actions automatically** updates the public search interface

### Quality Standards
- ✅ Workflow must be functional and tested
- ✅ Remove all credentials and sensitive data
- ✅ Follow naming convention for consistency
- ✅ Verify compatibility with recent n8n versions
- ✅ Include meaningful description or comments
- ✅ Add relevant tags for search optimization

### Custom Node Workflows
- ✅ Include npm package links in descriptions
- ✅ Document custom node requirements
- ✅ Add installation instructions
- ✅ Use descriptive tags (like CalcsLive example)

### Reindexing (for local development)
```bash
# Force database reindexing after adding workflows
python run.py --reindex

# Or update search index only
python scripts/generate_search_index.py
```

---

## ⚠️ Important Notes

### Security & Privacy
- **Review before use** - All workflows shared as-is for educational purposes
- **Update credentials** - Replace API keys, tokens, and webhooks
- **Test safely** - Verify in development environment first
- **Check permissions** - Ensure proper access rights for integrations

### Compatibility
- **n8n Version** - Compatible with n8n 1.0+ (most workflows)
- **Community Nodes** - Some workflows may require additional node installations
- **API Changes** - External services may have updated their APIs since creation
- **Dependencies** - Verify required integrations before importing

---

## 📚 Resources & References

### Workflow Sources
This comprehensive collection includes workflows from:
- **Official n8n.io** - Documentation and community examples
- **GitHub repositories** - Open source community contributions  
- **Blog posts & tutorials** - Real-world automation patterns
- **User submissions** - Tested and verified workflows
- **Enterprise use cases** - Business process automations

### Learn More
- [n8n Documentation](https://docs.n8n.io/) - Official documentation
- [n8n Community](https://community.n8n.io/) - Community forum and support
- [Workflow Templates](https://n8n.io/workflows/) - Official template library
- [Integration Docs](https://docs.n8n.io/integrations/) - Service-specific guides

---

## 🏆 Project Achievements

### Repository Transformation
- **2,053 workflows** professionally organized and named
- **365 unique integrations** automatically detected and categorized
- **100% meaningful names** (improved from basic filename patterns)
- **Zero data loss** during intelligent renaming process
- **Advanced search** with 15 service categories

### Performance Revolution
- **Sub-100ms search** with SQLite FTS5 full-text indexing
- **Instant filtering** across 29,445 workflow nodes
- **Mobile-optimized** responsive design for all devices
- **Real-time statistics** with live database queries
- **Professional interface** with modern UX principles

### System Reliability
- **Robust error handling** with graceful degradation
- **Change detection** for efficient database updates
- **Background processing** for non-blocking operations
- **Comprehensive logging** for debugging and monitoring
- **Production-ready** with proper middleware and security

---

*This repository represents the most comprehensive and well-organized collection of n8n workflows available, featuring cutting-edge search technology and professional documentation that makes workflow discovery and usage a delightful experience.*

**🎯 Perfect for**: Developers, automation engineers, business analysts, and anyone looking to streamline their workflows with proven n8n automations.

---

[中文](./README_ZH.md)



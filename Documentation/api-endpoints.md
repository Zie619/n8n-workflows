# N8N Workflow API Endpoints Documentation

## Base URL
```
https://scan-might-updates-postage.trycloudflare.com/api
```

## Available Endpoints

### 1. Statistics Endpoint
**URL:** `/api/stats`  
**Method:** GET  
**Description:** Returns overall repository statistics

**Response Structure:**
```json
{
  "total": 2055,
  "active": 215,
  "inactive": 1840,
  "triggers": {
    "Manual": 1234,
    "Webhook": 456,
    "Scheduled": 234,
    "Complex": 131
  },
  "complexity": {
    "low": 1456,
    "medium": 456,
    "high": 143
  },
  "total_nodes": 29518,
  "unique_integrations": 365,
  "last_indexed": "2025-07-27 17:40:54"
}
```

### 2. Workflow Search Endpoint
**URL:** `/api/workflows`  
**Method:** GET  
**Description:** Search and paginate through workflows

**Query Parameters:**
- `q` (string): Search query (default: '')
- `trigger` (string): Filter by trigger type - 'all', 'Webhook', 'Scheduled', 'Manual', 'Complex' (default: 'all')
- `complexity` (string): Filter by complexity - 'all', 'low', 'medium', 'high' (default: 'all')
- `active_only` (boolean): Show only active workflows (default: false)
- `page` (integer): Page number (default: 1)
- `per_page` (integer): Results per page, max 100 (default: 20)

**Example Request:**
```bash
curl "https://scan-might-updates-postage.trycloudflare.com/api/workflows?per_page=100&page=1"
```

**Response Structure:**
```json
{
  "workflows": [
    {
      "id": 102,
      "filename": "example.json",
      "name": "Example Workflow",
      "workflow_id": "",
      "active": 0,
      "description": "Example description",
      "trigger_type": "Manual",
      "complexity": "medium",
      "node_count": 6,
      "integrations": ["HTTP", "Google Sheets"],
      "tags": [],
      "created_at": "",
      "updated_at": "",
      "file_hash": "...",
      "file_size": 4047,
      "analyzed_at": "2025-07-27 17:40:54"
    }
  ],
  "total": 2055,
  "page": 1,
  "per_page": 100,
  "pages": 21,
  "query": "",
  "filters": {
    "trigger": "all",
    "complexity": "all",
    "active_only": false
  }
}
```

### 3. Individual Workflow Detail Endpoint
**URL:** `/api/workflows/{filename}`  
**Method:** GET  
**Description:** Get detailed information about a specific workflow

**Example Request:**
```bash
curl "https://scan-might-updates-postage.trycloudflare.com/api/workflows/0150_Awsrekognition_GoogleSheets_Automation_Webhook.json"
```

**Response Structure:**
```json
{
  "metadata": {
    "id": 102,
    "filename": "0150_Awsrekognition_GoogleSheets_Automation_Webhook.json",
    "name": "Awsrekognition Googlesheets Automation Webhook",
    "workflow_id": "",
    "active": 0,
    "description": "Manual workflow that orchestrates Httprequest, Google Sheets, and Awsrekognition for data processing. Uses 6 nodes.",
    "trigger_type": "Manual",
    "complexity": "medium",
    "node_count": 6,
    "integrations": ["Httprequest", "Google Sheets", "Awsrekognition"],
    "tags": [],
    "created_at": "",
    "updated_at": "",
    "file_hash": "74bdca251ec3446c2f470c17024beccd",
    "file_size": 4047,
    "analyzed_at": "2025-07-27 17:40:54"
  },
  "raw_json": {
    "nodes": [...],
    "connections": {...}
  }
}
```

**Important:** The actual workflow metadata is nested under the `metadata` key, not at the root level.

### 4. Categories Endpoint
**URL:** `/api/categories`  
**Method:** GET  
**Description:** Get list of available workflow categories

**Response Structure:**
```json
{
  "categories": [
    "AI Agent Development",
    "Business Process Automation", 
    "CRM & Sales",
    "Cloud Storage & File Management",
    "Communication & Messaging",
    "Creative Content & Video Automation",
    "Creative Design Automation",
    "Data Processing & Analysis",
    "E-commerce & Retail",
    "Financial & Accounting",
    "Marketing & Advertising Automation",
    "Project Management",
    "Social Media Management",
    "Technical Infrastructure & DevOps",
    "Uncategorized",
    "Web Scraping & Data Extraction"
  ]
}
```

### 5. Category Mappings Endpoint
**URL:** `/api/category-mappings`  
**Method:** GET  
**Description:** Get complete mapping of workflow filenames to categories

**Response Structure:**
```json
{
  "mappings": {
    "0001_Telegram_Schedule_Automation_Scheduled.json": "Communication & Messaging",
    "0002_Manual_Totp_Automation_Triggered.json": "Uncategorized",
    "0003_Bitwarden_Automate.json": "Uncategorized",
    "...": "...",
    "workflow_filename.json": "Category Name"
  }
}
```

**Total Mappings:** 2,055 filename-to-category mappings

### 6. Download Workflow Endpoint
**URL:** `/api/workflows/{filename}/download`  
**Method:** GET  
**Description:** Download the raw JSON file for a workflow

**Response:** Raw JSON workflow file with appropriate headers for download

### 7. Workflow Diagram Endpoint
**URL:** `/api/workflows/{filename}/diagram`  
**Method:** GET  
**Description:** Generate a Mermaid diagram representation of the workflow

**Response Structure:**
```json
{
  "diagram": "graph TD\n    node1[\"Node Name\\n(Type)\"]\n    node1 --> node2\n    ..."
}
```

## Usage Examples

### Get Business Process Automation Workflows
```bash
# Step 1: Get category mappings
curl -s "https://scan-might-updates-postage.trycloudflare.com/api/category-mappings" \
  | jq -r '.mappings | to_entries | map(select(.value == "Business Process Automation")) | .[].key'

# Step 2: For each filename, get details
curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows/{filename}" \
  | jq '.metadata'
```

### Search for Specific Workflows
```bash
# Search for workflows containing "calendar"
curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows?q=calendar&per_page=50"

# Get only webhook-triggered workflows
curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows?trigger=Webhook&per_page=100"

# Get only active workflows
curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows?active_only=true&per_page=100"
```

### Pagination Through All Workflows
```bash
# Get total pages
total_pages=$(curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows?per_page=100&page=1" | jq '.pages')

# Loop through all pages
for page in $(seq 1 $total_pages); do
  curl -s "https://scan-might-updates-postage.trycloudflare.com/api/workflows?per_page=100&page=${page}"
done
```

## Rate Limiting and Best Practices

### Recommended Practices
- Use small delays between requests (0.05-0.1 seconds)
- Process in batches by category for better organization
- Handle JSON parsing errors gracefully
- Validate response structure before processing

### Performance Tips
- Use `per_page=100` for maximum efficiency
- Cache category mappings for multiple operations
- Process categories in parallel if needed
- Use jq for efficient JSON processing

## Error Handling

### Common Response Codes
- `200`: Success
- `404`: Workflow not found
- `500`: Server error
- `408`: Request timeout

### Error Response Structure
```json
{
  "error": "Error message",
  "details": "Additional error details"
}
```

## Data Quality Notes

### Known Issues
1. Some workflow names may be generic (e.g., "My workflow")
2. Integration names are extracted from node types and may vary in formatting
3. Descriptions are auto-generated and may not reflect actual workflow purpose
4. Active status indicates workflow configuration, not actual usage

### Data Reliability
- **File hashes**: Reliable for detecting changes
- **Node counts**: Accurate
- **Integration lists**: Generally accurate but may include core n8n components
- **Complexity ratings**: Based on node count (≤5: low, 6-15: medium, 16+: high)
- **Categories**: Human-curated and reliable
# API Documentation: Workflow dashboard with mermaid.js

## Overview
Automated workflow: Workflow dashboard with mermaid.js. This workflow integrates 10 different services: webhook, stickyNote, code, n8n, switch. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `dd9e2c5d-6c48-428e-aa54-bef9e369d3b0`
- **Method**: `POST`
- **Webhook ID**: `dd9e2c5d-6c48-428e-aa54-bef9e369d3b0`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`

## Environment Variables
- No environment variables required

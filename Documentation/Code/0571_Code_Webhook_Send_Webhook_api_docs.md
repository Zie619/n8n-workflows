# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 9 different services: webhook, stickyNote, airtable, code, scheduleTrigger. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `e9e62c98-390d-4d16-bc77-a13b043bf1cf`
- **Method**: `POST`
- **Webhook ID**: `e9e62c98-390d-4d16-bc77-a13b043bf1cf`


## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.html`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`

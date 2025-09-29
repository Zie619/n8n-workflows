# API Documentation: Track Working Time and Pauses

## Overview
Automated workflow: Track Working Time and Pauses. This workflow integrates 8 different services: webhook, stickyNote, switch, set, respondToWebhook. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `track-time`
- **Method**: `POST`
- **Webhook ID**: `752a7723-87b6-470f-a7d3-f627f6457e39`


## Node Types Used
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`

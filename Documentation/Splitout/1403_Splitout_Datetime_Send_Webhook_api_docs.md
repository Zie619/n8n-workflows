# API Documentation: Send Emails from Obsidian

## Overview
Automated workflow: Send Emails from Obsidian. This workflow integrates 12 different services: convertToFile, stickyNote, webhook, splitOut, respondToWebhook. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `e634d721-48b0-4985-8a57-62ca4c7b3cfb`
- **Method**: `POST`
- **Webhook ID**: `e634d721-48b0-4985-8a57-62ca4c7b3cfb`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- No environment variables required

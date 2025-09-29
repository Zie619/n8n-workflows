# API Documentation: Crypto Workflow

## Overview
Automated workflow: Crypto Workflow. This workflow integrates 9 different services: webhook, filemaker, stickyNote, respondToWebhook, set. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `4cf50a61-b550-4ee6-984d-ad8c94e2b5c2`
- **Method**: `POST`
- **Webhook ID**: `4cf50a61-b550-4ee6-984d-ad8c94e2b5c2`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.moveBinaryData`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.filemaker`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `fileMaker`

## Environment Variables
- No environment variables required

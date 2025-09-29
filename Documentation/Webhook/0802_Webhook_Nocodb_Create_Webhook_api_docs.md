# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 10 different services: webhook, stickyNote, dropbox, merge, switch. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `29a6482f-36ac-4c15-8792-450aa32cf5f4`
- **Method**: `['POST', 'GET']`
- **Webhook ID**: `29a6482f-36ac-4c15-8792-450aa32cf5f4`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.nocoDb`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.set`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.dropbox`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `dropboxOAuth2Api`
- `nocoDbApiToken`

## Environment Variables
- No environment variables required

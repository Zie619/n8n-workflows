# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 6 different services: webhook, stickyNote, httpRequest, set, respondToWebhook. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `createMaskedEmail`
- **Method**: `POST`
- **Webhook ID**: `87f9abd1-2c9b-4d1f-8c7f-2261f4698c3c`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`

## Environment Variables
- `API_BASE_URL`

# API Documentation: Get all scaleway server info copy

## Overview
Automated workflow: Get all scaleway server info copy. This workflow integrates 11 different services: webhook, stickyNote, httpRequest, code, splitOut. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 89
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `a6767312-3a4c-4819-b4fe-a03c9e0ade5c`
- **Method**: `POST`
- **Webhook ID**: `a6767312-3a4c-4819-b4fe-a03c9e0ade5c`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpBasicAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

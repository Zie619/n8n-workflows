# API Documentation: If Workflow

## Overview
Automated workflow: If Workflow. This workflow integrates 6 different services: webhook, stickyNote, httpRequest, respondToWebhook, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `generate-voice`
- **Method**: `POST`
- **Webhook ID**: `5acc6769-6c0f-42a8-a69c-b05e437e18a9`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpCustomAuth`

## Environment Variables
- `BASE_URL`

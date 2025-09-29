# API Documentation: comentarios automaticos

## Overview
Automated workflow: comentarios automaticos. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, filter, agent. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ea7d37ac-9e82-40d7-bbb3-e9b7ce180fc9`
- **Method**: `POST`
- **Webhook ID**: `ea7d37ac-9e82-40d7-bbb3-e9b7ce180fc9`

- **Path**: `ea7d37ac-9e82-40d7-bbb3-e9b7ce180fc9`
- **Method**: `POST`
- **Webhook ID**: `ea7d37ac-9e82-40d7-bbb3-e9b7ce180fc9`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openRouterApi`
- `facebookGraphApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

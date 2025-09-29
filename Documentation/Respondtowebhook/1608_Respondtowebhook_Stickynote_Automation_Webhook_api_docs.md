# API Documentation: chrome extension backend with AI

## Overview
Automated workflow: chrome extension backend with AI. This workflow integrates 5 different services: webhook, stickyNote, respondToWebhook, stopAndError, openAi. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `e9a97dd5-f1e7-4d5b-a6f1-be5f0c9eb96c`
- **Method**: `POST`
- **Webhook ID**: `e9a97dd5-f1e7-4d5b-a6f1-be5f0c9eb96c`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required

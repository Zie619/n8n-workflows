# API Documentation: Dynamically generate HTML page from user request using OpenAI Structured Output

## Overview
Automated workflow: Dynamically generate HTML page from user request using OpenAI Structured Output. This workflow integrates 7 different services: webhook, stickyNote, httpRequest, respondToWebhook, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `d962c916-6369-431a-9d80-af6e6a50fdf5`
- **Method**: `POST`
- **Webhook ID**: `d962c916-6369-431a-9d80-af6e6a50fdf5`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.html`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- `API_BASE_URL`

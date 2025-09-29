# API Documentation: Get Airtable data in Obsidian Notes

## Overview
Automated workflow: Get Airtable data in Obsidian Notes. This workflow integrates 7 different services: webhook, stickyNote, agent, respondToWebhook, stopAndError. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `59fc8248-d3f7-4dbc-bdf3-39d59e427160`
- **Method**: `POST`
- **Webhook ID**: `59fc8248-d3f7-4dbc-bdf3-39d59e427160`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.airtableTool`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`

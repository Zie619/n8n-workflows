# API Documentation: Lmchatopenai Workflow

## Overview
Automated workflow: Lmchatopenai Workflow. This workflow integrates 6 different services: webhook, stickyNote, agent, respondToWebhook, stopAndError. It contains 12 nodes and follows best practices for error handling and security.

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
- **Path**: `assistant`
- **Method**: `POST`
- **Webhook ID**: `f0224b4b-1644-4d3d-9f12-01a9c04879e4`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required

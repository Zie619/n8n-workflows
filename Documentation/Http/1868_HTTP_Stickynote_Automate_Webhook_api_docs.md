# API Documentation: Chatbot AI

## Overview
Automated workflow: Chatbot AI. This workflow integrates 8 different services: webhook, stickyNote, httpRequest, agent, set. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `AIChatbot`
- **Method**: `POST`
- **Webhook ID**: `c69b940a-5a44-45e3-b9b4-04abda6462b2`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.lmChatAzureOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`
- `azureOpenAiApi`

## Environment Variables
- `API_BASE_URL`

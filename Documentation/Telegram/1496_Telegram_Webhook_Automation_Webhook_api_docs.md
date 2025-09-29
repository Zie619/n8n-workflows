# API Documentation: 🔍🛠️Perplexity Researcher to HTML Web Page

## Overview
Automated workflow: 🔍🛠️Perplexity Researcher to HTML Web Page. This workflow integrates 15 different services: webhook, stickyNote, httpRequest, telegram, agent. It contains 60 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 77
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.executeWorkflowTrigger`

### Webhook Endpoints
- **Path**: `pblog`
- **Method**: `POST`
- **Webhook ID**: `6a8e3ae7-02ae-4663-a27a-07df448550ab`


## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`
- `httpHeaderAuth`
- `httpCustomAuth`

## Environment Variables
- `API_BASE_URL`

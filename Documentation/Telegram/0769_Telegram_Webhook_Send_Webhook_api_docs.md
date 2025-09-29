# API Documentation: Memorybufferwindow Workflow

## Overview
Automated workflow: Memorybufferwindow Workflow. This workflow integrates 18 different services: webhook, telegramTrigger, httpRequest, stickyNote, telegram. It contains 50 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 71
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.scheduleTrigger`

### Webhook Endpoints
- **Path**: `12a80fbc-ac59-48f3-b6fd-683d7c420995`
- **Method**: `POST`
- **Webhook ID**: `12a80fbc-ac59-48f3-b6fd-683d7c420995`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.airtableTool`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`
- `httpHeaderAuth`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

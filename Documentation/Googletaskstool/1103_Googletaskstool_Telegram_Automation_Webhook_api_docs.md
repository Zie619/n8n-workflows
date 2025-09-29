# API Documentation: agente

## Overview
Automated workflow: agente. This workflow integrates 19 different services: convertToFile, stickyNote, scheduleTrigger, switch, lmChatOpenAi. It contains 56 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 77
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `evolutionAPIKORE`
- **Method**: `POST`
- **Webhook ID**: `405dab7c-a0ea-4f5b-a6cc-ede9d5ba78a0`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.googleTasksTool`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.telegramTool`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.telegramTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-evolution-api.evolutionApi`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `evolutionApi`
- `googleTasksOAuth2Api`
- `openRouterApi`
- `telegramApi`
- `postgres`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

# API Documentation: AI Phone Agent with RetellAI

## Overview
Automated workflow: AI Phone Agent with RetellAI. This workflow integrates 20 different services: stickyNote, vectorStoreQdrant, lmChatOpenAi, chainLlm, documentDefaultDataLoader. It contains 58 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 87
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `edb1e894-1210-4902-a34f-a014bbdad8d8`
- **Method**: `POST`
- **Webhook ID**: `edb1e894-1210-4902-a34f-a014bbdad8d8`

- **Path**: `b352dd49-d3b3-4e0a-a781-17137f7199c8`
- **Method**: `POST`
- **Webhook ID**: `b352dd49-d3b3-4e0a-a781-17137f7199c8`

- **Path**: `4dcd68b1-91d3-40bc-8aa6-c681126752b2`
- **Method**: `POST`
- **Webhook ID**: `4dcd68b1-91d3-40bc-8aa6-c681126752b2`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `googleCalendarOAuth2Api`
- `googleDriveOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`

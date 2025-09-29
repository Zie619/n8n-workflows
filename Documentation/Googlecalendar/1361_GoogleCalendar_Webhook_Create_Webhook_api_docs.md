# API Documentation: Build a Chatbot, Voice Agent and Phone Agent with Voiceflow, Google Calendar and RAG

## Overview
Automated workflow: Build a Chatbot, Voice Agent and Phone Agent with Voiceflow, Google Calendar and RAG. This workflow integrates 18 different services: webhook, stickyNote, httpRequest, textSplitterTokenSplitter, vectorStoreQdrant. It contains 60 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 101
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `9ff7a394-5b4b-4790-a96b-c41c4ba27fa5`
- **Method**: `POST`
- **Webhook ID**: `9ff7a394-5b4b-4790-a96b-c41c4ba27fa5`

- **Path**: `f5edfe92-649b-40da-ab35-f818ccb55ad4`
- **Method**: `POST`
- **Webhook ID**: `f5edfe92-649b-40da-ab35-f818ccb55ad4`

- **Path**: `edb1e894-1210-4902-a34f-a014bbdad8d8`
- **Method**: `POST`
- **Webhook ID**: `edb1e894-1210-4902-a34f-a014bbdad8d8`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.set`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `googleCalendarOAuth2Api`
- `httpHeaderAuth`
- `googleDriveOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

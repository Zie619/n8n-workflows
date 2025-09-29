# API Documentation: Business WhatsApp AI RAG Chatbot

## Overview
Automated workflow: Business WhatsApp AI RAG Chatbot. This workflow integrates 16 different services: webhook, stickyNote, httpRequest, textSplitterTokenSplitter, vectorStoreQdrant. It contains 38 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 63
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `f0d2e6f6-8fda-424d-b377-0bd191343c20`
- **Method**: `POST`
- **Webhook ID**: `f0d2e6f6-8fda-424d-b377-0bd191343c20`

- **Path**: `f0d2e6f6-8fda-424d-b377-0bd191343c20`
- **Method**: `POST`
- **Webhook ID**: `f0d2e6f6-8fda-424d-b377-0bd191343c20`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.whatsApp`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `googleDriveOAuth2Api`
- `whatsAppApi`

## Environment Variables
- `WEBHOOK_URL`

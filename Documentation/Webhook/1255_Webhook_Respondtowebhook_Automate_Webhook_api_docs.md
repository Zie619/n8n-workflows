# API Documentation: Stock Q&A Workflow

## Overview
Automated workflow: Stock Q&A Workflow. This workflow integrates 14 different services: webhook, stickyNote, textSplitterRecursiveCharacterTextSplitter, chainRetrievalQa, vectorStoreQdrant. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.manualChatTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `19f5499a-3083-4783-93a0-e8ed76a9f742`
- **Method**: `POST`
- **Webhook ID**: `679f4afb-189e-4f04-9dc0-439eec2ec5f1`


## Node Types Used
- `@n8n/n8n-nodes-langchain.documentBinaryInputLoader`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `@n8n/n8n-nodes-langchain.manualChatTrigger`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `qdrantApi`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`

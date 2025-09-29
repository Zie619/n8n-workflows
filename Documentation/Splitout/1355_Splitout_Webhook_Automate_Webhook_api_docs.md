# API Documentation: Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration

## Overview
Automated workflow: Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration. This workflow integrates 22 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, vectorStoreQdrant, chainRetrievalQa, merge. It contains 57 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 106
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.executeWorkflowTrigger`

### Webhook Endpoints
- **Path**: `bitrix24/openchannel-rag-bothandler.php`
- **Method**: `POST`
- **Webhook ID**: `bde38660-2604-4e00-afc0-5ebceebb7f0a`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.function`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.embeddingsOllama`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`

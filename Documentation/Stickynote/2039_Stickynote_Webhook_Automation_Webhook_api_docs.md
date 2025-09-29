# API Documentation: Travel AssistantAgent

## Overview
Automated workflow: Travel AssistantAgent. This workflow integrates 11 different services: webhook, stickyNote, textSplitterRecursiveCharacterTextSplitter, lmChatGoogleGemini, agent. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 28
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ingestData`
- **Method**: `POST`
- **Webhook ID**: `a48d5121-b453-4b5e-aa30-88ba3e16b931`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.vectorStoreMongoDBAtlas`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.memoryMongoDbChat`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `googlePalmApi`
- `mongoDb`

## Environment Variables
- No environment variables required

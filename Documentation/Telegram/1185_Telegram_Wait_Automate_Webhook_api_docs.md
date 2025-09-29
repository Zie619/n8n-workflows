# API Documentation: 🤖 AI Powered RAG Chatbot for Your Docs + Google Drive + Gemini + Qdrant

## Overview
Automated workflow: 🤖 AI Powered RAG Chatbot for Your Docs + Google Drive + Gemini + Qdrant. This workflow integrates 25 different services: stickyNote, vectorStoreQdrant, merge, lmChatOpenAi, if. It contains 66 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 75
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chatTrigger`

### Webhook Endpoints
- **Path**: `upsert`
- **Method**: `POST`
- **Webhook ID**: `3a30557f-9264-4bc8-a253-a9356677c791`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.code`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.summarize`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `googlePalmApi`
- `googleDocsOAuth2Api`
- `googleDriveOAuth2Api`
- `telegramApi`

## Environment Variables
- `BASE_URL`

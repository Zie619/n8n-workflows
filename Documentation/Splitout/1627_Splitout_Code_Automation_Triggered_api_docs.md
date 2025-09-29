# API Documentation: RAG:Context-Aware Chunking | Google Drive to Pinecone via OpenRouter & Gemini

## Overview
Automated workflow: RAG:Context-Aware Chunking | Google Drive to Pinecone via OpenRouter & Gemini. This workflow integrates 15 different services: stickyNote, vectorStorePinecone, embeddingsGoogleGemini, textSplitterRecursiveCharacterTextSplitter, code. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `openRouterApi`
- `googlePalmApi`
- `googleDriveOAuth2Api`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`

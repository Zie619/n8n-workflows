# API Documentation: Googledrive Workflow

## Overview
Automated workflow: Googledrive Workflow. This workflow integrates 13 different services: stickyNote, vectorStorePinecone, textSplitterRecursiveCharacterTextSplitter, chainRetrievalQa, googleDrive. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`

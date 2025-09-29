# API Documentation: RAG Workflow For Company Documents stored in Google Drive

## Overview
Automated workflow: RAG Workflow For Company Documents stored in Google Drive. This workflow integrates 13 different services: stickyNote, vectorStorePinecone, embeddingsGoogleGemini, googleDriveTrigger, textSplitterRecursiveCharacterTextSplitter. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googlePalmApi`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`

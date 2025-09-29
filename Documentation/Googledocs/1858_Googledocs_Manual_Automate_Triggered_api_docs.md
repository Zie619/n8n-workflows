# API Documentation: RAG Workflow For Stock Earnings Report Analysis

## Overview
Automated workflow: RAG Workflow For Stock Earnings Report Analysis. This workflow integrates 15 different services: stickyNote, vectorStorePinecone, embeddingsGoogleGemini, textSplitterRecursiveCharacterTextSplitter, lmChatGoogleGemini. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
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

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `googlePalmApi`
- `googleDocsOAuth2Api`
- `googleDriveOAuth2Api`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

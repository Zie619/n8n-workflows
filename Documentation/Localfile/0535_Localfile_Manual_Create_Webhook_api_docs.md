# API Documentation: Localfiletrigger Workflow

## Overview
Automated workflow: Localfiletrigger Workflow. This workflow integrates 17 different services: stickyNote, httpRequest, embeddingsMistralCloud, textSplitterRecursiveCharacterTextSplitter, chainRetrievalQa. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 60
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.localFileTrigger`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatMistralCloud`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.localFileTrigger`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.embeddingsMistralCloud`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `mistralCloudApi`
- `qdrantApi`

## Environment Variables
- `BASE_URL`

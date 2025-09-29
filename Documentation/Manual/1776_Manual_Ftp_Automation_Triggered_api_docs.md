# API Documentation: Qdrant Vector Database Embedding Pipeline

## Overview
Automated workflow: Qdrant Vector Database Embedding Pipeline. This workflow integrates 9 different services: stickyNote, vectorStoreQdrant, ftp, documentDefaultDataLoader, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.textSplitterCharacterTextSplitter`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.ftp`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `ftp`

## Environment Variables
- No environment variables required

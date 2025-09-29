# API Documentation: Localfiletrigger Workflow

## Overview
Automated workflow: Localfiletrigger Workflow. This workflow integrates 23 different services: convertToFile, stickyNote, embeddingsMistralCloud, textSplitterRecursiveCharacterTextSplitter, lmChatMistralCloud. It contains 49 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 54
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.localFileTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `@n8n/n8n-nodes-langchain.lmChatMistralCloud`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.localFileTrigger`
- `@n8n/n8n-nodes-langchain.outputParserItemList`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.splitInBatches`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.embeddingsMistralCloud`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `mistralCloudApi`
- `qdrantApi`

## Environment Variables
- No environment variables required

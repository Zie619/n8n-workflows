# API Documentation: My workflow 3

## Overview
Automated workflow: My workflow 3. This workflow integrates 21 different services: convertToFile, stickyNote, embeddingsMistralCloud, textSplitterRecursiveCharacterTextSplitter, chainRetrievalQa. It contains 50 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 67
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitInBatches`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.embeddingsMistralCloud`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

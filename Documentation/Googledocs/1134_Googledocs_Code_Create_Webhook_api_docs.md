# API Documentation: Generate Exam Questions

## Overview
Automated workflow: Generate Exam Questions. This workflow integrates 21 different services: convertToFile, stickyNote, vectorStoreQdrant, chainRetrievalQa, splitInBatches. It contains 53 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 66
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.outputParserItemList`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `googlePalmApi`
- `googleSheetsOAuth2Api`
- `googleDocsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

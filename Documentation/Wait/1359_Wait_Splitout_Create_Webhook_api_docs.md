# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 22 different services: stickyNote, embeddingsMistralCloud, textSplitterRecursiveCharacterTextSplitter, vectorStoreQdrant, switch. It contains 48 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 69
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.compression`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.embeddingsMistralCloud`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `mistralCloudApi`
- `openAiApi`
- `qdrantApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

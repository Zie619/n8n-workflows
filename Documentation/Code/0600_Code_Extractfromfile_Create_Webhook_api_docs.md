# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 31 different services: convertToFile, stickyNote, textSplitterRecursiveCharacterTextSplitter, airtable, vectorStoreQdrant. It contains 65 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 82
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.airtableTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.compression`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.executeWorkflow`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.airtableTool`
- `n8n-nodes-base.editImage`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.sort`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

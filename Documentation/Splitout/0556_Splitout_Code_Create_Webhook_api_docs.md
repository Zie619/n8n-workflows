# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 18 different services: filter, httpRequest, stickyNote, vectorStoreQdrant, textSplitterRecursiveCharacterTextSplitter. It contains 45 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 62
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.hackerNews`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.executeWorkflow`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

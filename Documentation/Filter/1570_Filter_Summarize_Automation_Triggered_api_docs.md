# API Documentation: Prod: Notion to Vector Store - Dimension 768

## Overview
Automated workflow: Prod: Notion to Vector Store - Dimension 768. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.notionTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `n8n-nodes-base.notionTrigger`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `notionApi`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`

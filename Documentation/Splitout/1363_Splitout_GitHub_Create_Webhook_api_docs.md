# API Documentation: Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

## Overview
Automated workflow: Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI. This workflow integrates 20 different services: stickyNote, vectorStoreQdrant, merge, lmChatOpenAi, github. It contains 38 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 59
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.github`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- Github

## Required Credentials
- `openAiApi`
- `githubApi`
- `qdrantApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

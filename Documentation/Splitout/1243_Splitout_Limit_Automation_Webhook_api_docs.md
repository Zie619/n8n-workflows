# API Documentation: Agent Milvus tool

## Overview
Automated workflow: Agent Milvus tool. This workflow integrates 14 different services: stickyNote, httpRequest, textSplitterRecursiveCharacterTextSplitter, agent, splitOut. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.limit`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreMilvus`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `milvusApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

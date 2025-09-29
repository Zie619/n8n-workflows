# API Documentation: Slack Workflow

## Overview
Automated workflow: Slack Workflow. This workflow integrates 23 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, chainRetrievalQa, lmChatOpenAi, if. It contains 52 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 73
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `74facfd7-0f51-4605-9724-2c300594fcf9`
- **Method**: `POST`
- **Webhook ID**: `74facfd7-0f51-4605-9724-2c300594fcf9`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmailTrigger`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmail`

## Integrations
- Slack

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

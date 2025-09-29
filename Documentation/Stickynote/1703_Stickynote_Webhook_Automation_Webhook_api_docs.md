# API Documentation: Travel Planning Agent with Couchbase Vector Search, Gemini 2.0 Flash and OpenAI

## Overview
Automated workflow: Travel Planning Agent with Couchbase Vector Search, Gemini 2.0 Flash and OpenAI. This workflow integrates 11 different services: webhook, stickyNote, textSplitterRecursiveCharacterTextSplitter, vectorStoreCouchbaseSearch, lmChatGoogleGemini. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 27
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `3ca6fbdd-a157-4e9d-9042-237048da85b6`
- **Method**: `POST`
- **Webhook ID**: `3ca6fbdd-a157-4e9d-9042-237048da85b6`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-couchbase.vectorStoreCouchbaseSearch`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required

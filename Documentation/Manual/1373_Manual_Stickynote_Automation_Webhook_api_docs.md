# API Documentation: Chat with GitHub OpenAPI Specification using RAG (Pinecone and OpenAI)

## Overview
Automated workflow: Chat with GitHub OpenAPI Specification using RAG (Pinecone and OpenAI). This workflow integrates 13 different services: stickyNote, httpRequest, vectorStorePinecone, textSplitterRecursiveCharacterTextSplitter, agent. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
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
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `pineconeApi`

## Environment Variables
- `API_BASE_URL`

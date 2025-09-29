# API Documentation: e-mail Chatbot with both semantic and structured RAG, using Telegram and Pgvector

## Overview
Automated workflow: e-mail Chatbot with both semantic and structured RAG, using Telegram and Pgvector. This workflow integrates 16 different services: telegramTrigger, stickyNote, telegram, code, agent. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 28
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.vectorStorePGVector`
- `@n8n/n8n-nodes-langchain.embeddingsOllama`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`
- `postgres`
- `ollamaApi`

## Environment Variables
- No environment variables required

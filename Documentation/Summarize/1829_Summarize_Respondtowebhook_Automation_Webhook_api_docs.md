# API Documentation: Adaptive RAG

## Overview
Automated workflow: Adaptive RAG. This workflow integrates 13 different services: stickyNote, embeddingsGoogleGemini, vectorStoreQdrant, lmChatGoogleGemini, agent. It contains 48 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 57
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `googlePalmApi`

## Environment Variables
- No environment variables required

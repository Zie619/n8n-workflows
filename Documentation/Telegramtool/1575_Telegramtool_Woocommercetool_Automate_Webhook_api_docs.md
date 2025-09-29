# API Documentation: WooCommerce AI Chatbot Workflow for Post-Sales Support

## Overview
Automated workflow: WooCommerce AI Chatbot Workflow for Post-Sales Support. This workflow integrates 20 different services: stickyNote, vectorStoreQdrant, lmChatOpenAi, chatTrigger, telegramTool. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 61
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.wooCommerceTool`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.telegramTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `httpBasicAuth`
- `wooCommerceApi`
- `googleDriveOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

# API Documentation: Chattrigger Workflow

## Overview
Automated workflow: Chattrigger Workflow. This workflow integrates 18 different services: stickyNote, textSplitterTokenSplitter, splitInBatches, vectorStoreQdrant, agent. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.zendesk`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Zendesk
- Zendesk

## Required Credentials
- `googleDriveOAuth2Api`
- `qdrantApi`
- `openAiApi`
- `zendeskApi`

## Environment Variables
- `WEBHOOK_URL`

# API Documentation: Slack AI Chatbot with RAG for company staff

## Overview
Automated workflow: Slack AI Chatbot with RAG for company staff. This workflow integrates 15 different services: stickyNote, httpRequest, textSplitterTokenSplitter, vectorStoreQdrant, slackTrigger. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.slackTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.slackTrigger`

## Integrations
- Slack
- Slack
- Google
- Google

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `googleDriveOAuth2Api`
- `anthropicApi`
- `slackApi`

## Environment Variables
- `WEBHOOK_URL`

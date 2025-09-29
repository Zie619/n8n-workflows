# API Documentation: AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs

## Overview
Automated workflow: AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs. This workflow integrates 12 different services: webhook, stickyNote, httpRequest, lmChatGoogleGemini, chainLlm. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `voice_message`
- **Method**: `POST`
- **Webhook ID**: `e9f611eb-a8dd-4520-8d24-9f36deaca528`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `googlePalmApi`
- `httpCustomAuth`

## Environment Variables
- `BASE_URL`

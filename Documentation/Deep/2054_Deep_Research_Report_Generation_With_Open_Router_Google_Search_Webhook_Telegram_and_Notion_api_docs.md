# API Documentation: Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion

## Overview
Automated workflow: Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion. This workflow integrates 22 different services: stickyNote, switch, splitInBatches, chainLlm, set. It contains 56 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 89
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `1c86c408-aeed-40c5-b4ba-aad5f4cdf0ad`
- **Method**: `POST`
- **Webhook ID**: `1c86c408-aeed-40c5-b4ba-aad5f4cdf0ad`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

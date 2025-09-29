# API Documentation: Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram

## Overview
Automated workflow: Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram. This workflow integrates 18 different services: webhook, telegramTrigger, stickyNote, telegram, code. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.telegramTrigger`

### Webhook Endpoints
- **Path**: `8f0beaaf-b2c3-4148-8006-3b73fa146f60`
- **Method**: `POST`
- **Webhook ID**: `8f0beaaf-b2c3-4148-8006-3b73fa146f60`


## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.googleDocs`
- `n8n-nodes-youtube-transcription-kasha.youtubeTranscripter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleDocsTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `telegramApi`
- `openAiApi`
- `googleDocsOAuth2Api`

## Environment Variables
- `BASE_URL`

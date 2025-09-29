# API Documentation: 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠

## Overview
Automated workflow: 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠. This workflow integrates 14 different services: webhook, stickyNote, telegram, agent, merge. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chatTrigger`

### Webhook Endpoints
- **Path**: `wbot`
- **Method**: `POST`
- **Webhook ID**: `097f36f3-1574-44f9-815f-58387e3b20bf`


## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleDocsTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `telegramApi`
- `googleDocsOAuth2Api`

## Environment Variables
- `BASE_URL`

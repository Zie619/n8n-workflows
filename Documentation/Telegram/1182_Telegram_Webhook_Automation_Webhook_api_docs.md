# API Documentation: 🤖 Telegram Messaging Agent for Text/Audio/Images

## Overview
Automated workflow: 🤖 Telegram Messaging Agent for Text/Audio/Images. This workflow integrates 13 different services: textClassifier, webhook, stickyNote, httpRequest, convertToFile. It contains 64 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 85
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `your-endpoint`
- **Method**: `POST`
- **Webhook ID**: `b4ed4c80-a655-4ff2-87d6-febd5280d343`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

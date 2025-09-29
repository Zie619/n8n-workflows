# API Documentation: Intelligent Web Query and Semantic Re-Ranking Flow

## Overview
Automated workflow: Intelligent Web Query and Semantic Re-Ranking Flow. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, code, lmChatGoogleGemini. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 52
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `962f1468-c80f-4c0c-8555-a0acf648ede4`
- **Method**: `POST`
- **Webhook ID**: `962f1468-c80f-4c0c-8555-a0acf648ede4`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `anthropicApi`
- `openAiApi`
- `googlePalmApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

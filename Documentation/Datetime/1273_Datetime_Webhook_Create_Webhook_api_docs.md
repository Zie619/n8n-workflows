# API Documentation: AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack

## Overview
Automated workflow: AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack. This workflow integrates 18 different services: textClassifier, webhook, stickyNote, httpRequest, markdown. It contains 41 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 54
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.scheduleTrigger`

### Webhook Endpoints
- **Path**: `4946fc26-bea4-4244-b37c-203c39537246`
- **Method**: `POST`
- **Webhook ID**: ``


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Slack

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `googleApi`
- `slackOAuth2Api`
- `wordpressApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

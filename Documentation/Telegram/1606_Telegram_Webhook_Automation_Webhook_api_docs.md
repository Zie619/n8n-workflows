# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 16 different services: webhook, stickyNote, httpRequest, telegramTrigger, toolHttpRequest. It contains 57 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 98
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `459d848d-72ed-490f-bc48-e5dc60242896`
- **Method**: `POST`
- **Webhook ID**: `459d848d-72ed-490f-bc48-e5dc60242896`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `telegramApi`
- `httpHeaderAuth`
- `googlePalmApi`
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

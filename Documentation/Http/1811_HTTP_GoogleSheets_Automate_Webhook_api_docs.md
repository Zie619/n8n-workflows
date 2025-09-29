# API Documentation: Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini

## Overview
Automated workflow: Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini. This workflow integrates 11 different services: webhook, stickyNote, httpRequest, lmChatGoogleGemini, agent. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `4c0de537-2889-47d2-ac44-3a9cda89c9f3`
- **Method**: `POST`
- **Webhook ID**: `4c0de537-2889-47d2-ac44-3a9cda89c9f3`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`
- `googlePalmApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

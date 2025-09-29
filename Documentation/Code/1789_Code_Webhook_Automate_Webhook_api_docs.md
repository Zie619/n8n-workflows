# API Documentation: (G) LineChatBot + Google Sheets (as a memory)

## Overview
Automated workflow: (G) LineChatBot + Google Sheets (as a memory). This workflow integrates 9 different services: webhook, stickyNote, httpRequest, code, lmChatGoogleGemini. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `guitarpa`
- **Method**: `POST`
- **Webhook ID**: `[CENSORED]`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
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
- `googlePalmApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

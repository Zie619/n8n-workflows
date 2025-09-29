# API Documentation: Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide

## Overview
Automated workflow: Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, filter, wait. It contains 30 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 51
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ebd11c9b-129c-4b59-8c27-9a4b567305f7`
- **Method**: `POST`
- **Webhook ID**: `ebd11c9b-129c-4b59-8c27-9a4b567305f7`

- **Path**: `f8878b78-43ea-4caa-b16c-cde9aaf2e9b1`
- **Method**: `POST`
- **Webhook ID**: `f8878b78-43ea-4caa-b16c-cde9aaf2e9b1`


## Node Types Used
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.twilio`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `gmailOAuth2`
- `twilioApi`
- `googleSheetsTriggerOAuth2Api`

## Environment Variables
- `API_BASE_URL`

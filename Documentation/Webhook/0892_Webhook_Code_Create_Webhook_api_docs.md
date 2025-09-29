# API Documentation: Openai Workflow

## Overview
Automated workflow: Openai Workflow. This workflow integrates 14 different services: webhook, filter, stickyNote, code, readPDF. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `cded3af3-31df-47c2-a826-ff84eb4a41df`
- **Method**: `POST`
- **Webhook ID**: `cded3af3-31df-47c2-a826-ff84eb4a41df`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.readPDF`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

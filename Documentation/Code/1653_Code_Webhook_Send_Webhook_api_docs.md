# API Documentation: Openai Workflow

## Overview
Automated workflow: Openai Workflow. This workflow integrates 15 different services: webhook, stickyNote, code, gmailTrigger, switch. It contains 58 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 71
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `e2aa55fb-618a-4478-805d-d6da46b908d1`
- **Method**: `POST`
- **Webhook ID**: `e2aa55fb-618a-4478-805d-d6da46b908d1`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.html`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

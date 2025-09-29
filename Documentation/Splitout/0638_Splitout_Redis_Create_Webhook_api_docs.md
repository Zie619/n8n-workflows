# API Documentation: If Workflow

## Overview
Automated workflow: If Workflow. This workflow integrates 17 different services: webhook, stickyNote, formTrigger, agent, splitOut. It contains 45 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 58
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ai-interview-transcripts/:session_id`
- **Method**: `POST`
- **Webhook ID**: `78df12c4-ccd0-46dd-be0d-4445c2bd04f2`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.form`
- `n8n-nodes-base.crypto`
- `@n8n/n8n-nodes-langchain.lmChatGroq`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.if`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `redis`
- `groqApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

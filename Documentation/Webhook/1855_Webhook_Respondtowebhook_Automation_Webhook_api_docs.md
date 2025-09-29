# API Documentation: Unique QRcode coupon assignment and validation for Lead Generation system

## Overview
Automated workflow: Unique QRcode coupon assignment and validation for Lead Generation system. This workflow integrates 10 different services: webhook, stickyNote, httpRequest, formTrigger, set. It contains 53 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 98
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `bb832325-8c58-4717-b866-41f8a9714cf2`
- **Method**: `POST`
- **Webhook ID**: `bb832325-8c58-4717-b866-41f8a9714cf2`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 5 different services: webhook, stickyNote, respondToWebhook, stopAndError, googleSheets. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `retell-dynamic-variables`
- **Method**: `POST`
- **Webhook ID**: `7f35a3a8-54c3-49d7-879d-6c3429f0e5da`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`

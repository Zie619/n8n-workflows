# API Documentation: Splitout Workflow

## Overview
Automated workflow: Splitout Workflow. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, splitOut, respondToWebhook. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ea568868-5770-4b2a-8893-700b344c995e`
- **Method**: `POST`
- **Webhook ID**: `ea568868-5770-4b2a-8893-700b344c995e`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`

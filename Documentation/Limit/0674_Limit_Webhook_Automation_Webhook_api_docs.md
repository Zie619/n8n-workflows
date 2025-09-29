# API Documentation: Gmailtrigger Workflow

## Overview
Automated workflow: Gmailtrigger Workflow. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, code, gmailTrigger. It contains 48 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 69
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `fb37cff7-b543-45f0-922d-4e0edcae5e43`
- **Method**: `POST`
- **Webhook ID**: `fb37cff7-b543-45f0-922d-4e0edcae5e43`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`

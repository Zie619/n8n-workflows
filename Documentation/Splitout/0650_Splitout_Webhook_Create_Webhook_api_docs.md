# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 14 different services: s3, webhook, stickyNote, httpRequest, splitOut. It contains 46 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 83
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `slack-image-upload-bot`
- **Method**: `POST`
- **Webhook ID**: `7f9dd2fb-e324-4f72-8fbf-d1f6b4fa5c79`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.s3`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `s3`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

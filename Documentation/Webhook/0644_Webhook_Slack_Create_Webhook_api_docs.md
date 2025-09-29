# API Documentation: Thehiveprojecttrigger Workflow

## Overview
Automated workflow: Thehiveprojecttrigger Workflow. This workflow integrates 12 different services: webhook, stickyNote, httpRequest, theHiveProjectTrigger, theHiveProject. It contains 94 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 155
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.theHiveProjectTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `slackthehivewebhook`
- **Method**: `POST`
- **Webhook ID**: `99db3e73-57d8-4107-ab02-5b7e713894ad`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.theHiveProjectTrigger`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.theHiveProject`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack
- Slack

## Required Credentials
- `slackApi`
- `theHiveProjectApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

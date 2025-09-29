# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 10 different services: webhook, itemLists, stickyNote, airtable, code. It contains 123 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 152
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `getslots`
- **Method**: `POST`
- **Webhook ID**: `42afdbc1-afd0-4d65-a713-cf7a59062d6c`

- **Path**: `bookslots`
- **Method**: `POST`
- **Webhook ID**: `42afdbc1-afd0-4d65-a713-cf7a59062d6c`

- **Path**: `updateslots`
- **Method**: `POST`
- **Webhook ID**: `66b278fe-97d1-4413-b6dd-4288d8ec66b2`

- **Path**: `cancelslots`
- **Method**: `POST`
- **Webhook ID**: `00fedd5a-c03d-4302-b8e0-22c79f26ed05`

- **Path**: `callresults`
- **Method**: `POST`
- **Webhook ID**: `4a6205cd-4277-4686-8008-540b802b99fe`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.code`
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
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

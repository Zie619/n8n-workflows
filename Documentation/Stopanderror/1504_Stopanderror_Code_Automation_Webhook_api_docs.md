# API Documentation: 2. Refresh Pipedrive tokens

## Overview
Automated workflow: 2. Refresh Pipedrive tokens. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, code, respondToWebhook. It contains 37 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 74
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `937a8843-a28a-400a-b473-bdc598366fa0`
- **Method**: `POST`
- **Webhook ID**: `937a8843-a28a-400a-b473-bdc598366fa0`

- **Path**: `47704458-bfa6-4d95-adf1-97fc78e35d8a`
- **Method**: `POST`
- **Webhook ID**: `47704458-bfa6-4d95-adf1-97fc78e35d8a`

- **Path**: `aae545fb-a69d-4e20-91ce-65f105d0ea2f`
- **Method**: `POST`
- **Webhook ID**: `aae545fb-a69d-4e20-91ce-65f105d0ea2f`


## Node Types Used
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpBasicAuth`
- `supabaseApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

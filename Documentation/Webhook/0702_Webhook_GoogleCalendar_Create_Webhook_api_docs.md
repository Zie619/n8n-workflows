# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 10 different services: webhook, stickyNote, httpRequest, airtable, respondToWebhook. It contains 62 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 119
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `9a52822c-0304-4dad-a86a-ae662161243c`
- **Method**: `POST`
- **Webhook ID**: `9a52822c-0304-4dad-a86a-ae662161243c`

- **Path**: `c1020b94-603c-4981-ab48-51e208d17223`
- **Method**: `POST`
- **Webhook ID**: `c1020b94-603c-4981-ab48-51e208d17223`

- **Path**: `9c15c8ac-8f3a-40d3-8ad5-e40468388968`
- **Method**: `POST`
- **Webhook ID**: `9c15c8ac-8f3a-40d3-8ad5-e40468388968`

- **Path**: `d9b20efe-9bb4-4d8b-b9aa-d568f43f78ea`
- **Method**: `POST`
- **Webhook ID**: `d9b20efe-9bb4-4d8b-b9aa-d568f43f78ea`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `zendeskApi`
- `googleCalendarOAuth2Api`
- `googleSheetsOAuth2Api`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

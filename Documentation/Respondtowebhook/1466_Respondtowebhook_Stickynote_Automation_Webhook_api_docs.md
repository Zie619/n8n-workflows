# API Documentation: TEMPLATE - Multi Methods API Endpoint

## Overview
Automated workflow: TEMPLATE - Multi Methods API Endpoint. This workflow integrates 5 different services: webhook, stickyNote, airtable, respondToWebhook, stopAndError. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 65
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `customers`
- **Method**: `POST`
- **Webhook ID**: `580ccc56-f308-4b64-961d-38323501a170`

- **Path**: `customers/:id`
- **Method**: `['GET', 'DELETE', 'PUT']`
- **Webhook ID**: `580ccc56-f308-4b64-961d-38323501a170`


## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`

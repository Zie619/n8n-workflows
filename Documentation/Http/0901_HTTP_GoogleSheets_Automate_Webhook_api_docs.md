# API Documentation: AccountCraft WhatsApp Automation - Infridet

## Overview
Automated workflow: AccountCraft WhatsApp Automation - Infridet. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `lead-capture`
- **Method**: `POST`
- **Webhook ID**: ``


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleApi`
- `httpBasicAuth`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

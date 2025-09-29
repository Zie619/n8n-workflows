# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 8 different services: webhook, stickyNote, httpRequest, set, stopAndError. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 50
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `d1e5fdd0-b51d-4447-8af3-6754017d240b`
- **Method**: `POST`
- **Webhook ID**: `d1e5fdd0-b51d-4447-8af3-6754017d240b`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `supabaseApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

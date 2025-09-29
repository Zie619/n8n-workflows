# API Documentation: Googlesheets Workflow

## Overview
Automated workflow: Googlesheets Workflow. This workflow integrates 11 different services: webhook, stickyNote, itemLists, code, merge. It contains 69 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 86
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `/approve-issue`
- **Method**: `POST`
- **Webhook ID**: `33876465-33a7-4cc1-bbb5-bc8c630edd9f`

- **Path**: `raw-materials-issue`
- **Method**: `POST`
- **Webhook ID**: `73d4bdfc-2d8b-42f4-85d5-43ecae0953c1`

- **Path**: `Pb-raw-materials`
- **Method**: `POST`
- **Webhook ID**: `be8290c0-bdd9-489e-938a-ba7a3dd5745e`


## Node Types Used
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`

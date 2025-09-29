# API Documentation: Notion to Clockify Sync Template

## Overview
Automated workflow: Notion to Clockify Sync Template. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, scheduleTrigger, merge. It contains 71 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 88
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.scheduleTrigger`

### Webhook Endpoints
- **Path**: `43028c1f-7331-4fbe-bf56-d6f47c92d9be`
- **Method**: `POST`
- **Webhook ID**: `43028c1f-7331-4fbe-bf56-d6f47c92d9be`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.clockify`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `notionApi`
- `clockifyApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

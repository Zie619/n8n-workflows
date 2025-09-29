# API Documentation: n8n Subworkflow Dependency Graph & Auto-Tagging

## Overview
Automated workflow: n8n Subworkflow Dependency Graph & Auto-Tagging. This workflow integrates 17 different services: webhook, filter, httpRequest, stickyNote, code. It contains 52 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 81
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.n8nTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `dependency-graph`
- **Method**: `POST`
- **Webhook ID**: `9ef127d4-bd1e-40db-999b-0881afbd2ab3`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.quickChart`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.n8nTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

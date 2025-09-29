# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 14 different services: webhook, itemLists, httpRequest, filter, wait. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 71
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.formTrigger`

### Webhook Endpoints
- **Path**: `d5124bd8-aada-44da-8050-3070f303ad24`
- **Method**: `POST`
- **Webhook ID**: `d5124bd8-aada-44da-8050-3070f303ad24`


## Node Types Used
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Slack

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

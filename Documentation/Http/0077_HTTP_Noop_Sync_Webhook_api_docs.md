# API Documentation: Syncro Alert to OpsGenie

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 7
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `fromsyncro`
- **Method**: `POST`
- **Webhook ID**: `fromsyncro`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`

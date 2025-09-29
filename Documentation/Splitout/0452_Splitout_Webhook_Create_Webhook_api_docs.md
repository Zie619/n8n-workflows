# API Documentation: Splitout Workflow

## Overview
Automated workflow: Splitout Workflow. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, splitOut, set. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `76a63718-b3cb-4141-bc55-efa614d13f1d`
- **Method**: `POST`
- **Webhook ID**: `76a63718-b3cb-4141-bc55-efa614d13f1d`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`

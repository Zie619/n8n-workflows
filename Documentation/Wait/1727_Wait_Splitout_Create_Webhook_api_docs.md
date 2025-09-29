# API Documentation: address validation

## Overview
Automated workflow: address validation. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, filter, wait. It contains 45 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 62
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `786e8a93-9837-44e6-81ae-a173ce25a14f`
- **Method**: `POST`
- **Webhook ID**: `786e8a93-9837-44e6-81ae-a173ce25a14f`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

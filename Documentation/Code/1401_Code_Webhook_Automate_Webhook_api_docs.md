# API Documentation: Workflow stats

## Overview
Automated workflow: Workflow stats. This workflow integrates 16 different services: webhook, stickyNote, code, n8n, merge. It contains 41 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 62
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `fb550a01-12f2-4709-ba2d-f71197b68340`
- **Method**: `POST`
- **Webhook ID**: `fb550a01-12f2-4709-ba2d-f71197b68340`

- **Path**: `73a91e4d-143d-4168-9efb-6c56f2258aec/dashboard.xsl`
- **Method**: `POST`
- **Webhook ID**: `73a91e4d-143d-4168-9efb-6c56f2258aec`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.moveBinaryData`
- `n8n-nodes-base.code`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.html`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`

## Environment Variables
- No environment variables required

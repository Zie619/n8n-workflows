# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 8 different services: s3, stickyNote, formTrigger, httpRequest, switch. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.s3`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`
- `s3`

## Environment Variables
- `API_BASE_URL`

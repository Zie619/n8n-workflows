# API Documentation: Basic PDF Digital Sign Service

## Overview
Automated workflow: Basic PDF Digital Sign Service. This workflow integrates 10 different services: convertToFile, webhook, stickyNote, code, readWriteFile. It contains 49 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 74
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `docu-digi-sign`
- **Method**: `POST`
- **Webhook ID**: `0c12b17f-77a7-46b2-99a0-432b29b58dfb`

- **Path**: `docu-download`
- **Method**: `POST`
- **Webhook ID**: `71854b24-a2b8-4cae-bb5d-3959f1573974`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required

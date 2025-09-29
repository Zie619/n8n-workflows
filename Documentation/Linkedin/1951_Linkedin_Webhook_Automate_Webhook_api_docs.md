# API Documentation: Training Feedback Automation

## Overview
Automated workflow: Training Feedback Automation. This workflow integrates 8 different services: airtableTrigger, webhook, stickyNote, linkedIn, httpRequest. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 66
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `4ff46f8a-e1d0-4ad9-8dae-99de53838aaf`
- **Method**: `POST`
- **Webhook ID**: `4ff46f8a-e1d0-4ad9-8dae-99de53838aaf`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.linkedIn`

## Integrations
- No external integrations detected

## Required Credentials
- `linkedInOAuth2Api`
- `smtp`
- `airtableOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

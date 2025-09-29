# API Documentation: Klicktipp Workflow

## Overview
Automated workflow: Klicktipp Workflow. This workflow integrates 9 different services: webhook, stickyNote, splitOut, merge, set. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `9e8feb6b-df09-4f17-baf0-9fa3b8c0093c`
- **Method**: `POST`
- **Webhook ID**: `9e8feb6b-df09-4f17-baf0-9fa3b8c0093c`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-klicktipp.klicktipp`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `klickTippApi`

## Environment Variables
- No environment variables required

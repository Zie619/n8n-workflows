# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 5 different services: webhook, stickyNote, httpRequest, set, stopAndError. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `e6d88547-5423-4b01-bc7f-e1f94274c4b2`
- **Method**: `POST`
- **Webhook ID**: `e6d88547-5423-4b01-bc7f-e1f94274c4b2`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `linearOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

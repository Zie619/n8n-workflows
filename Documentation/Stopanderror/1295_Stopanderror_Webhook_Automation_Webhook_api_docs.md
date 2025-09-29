# API Documentation: Auth0 User Login

## Overview
Automated workflow: Auth0 User Login. This workflow integrates 7 different services: webhook, stickyNote, httpRequest, respondToWebhook, stopAndError. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 46
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `login`
- **Method**: `POST`
- **Webhook ID**: `046e2370-0ae1-4d64-be9b-cbb0545de323`

- **Path**: `receive-token`
- **Method**: `POST`
- **Webhook ID**: `7bd9ea5a-c354-41c0-9d17-4a02ca8e3055`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`

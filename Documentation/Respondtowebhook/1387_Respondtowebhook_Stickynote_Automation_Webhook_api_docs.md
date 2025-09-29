# API Documentation: Image Generation API

## Overview
Automated workflow: Image Generation API. This workflow integrates 5 different services: webhook, stickyNote, respondToWebhook, stopAndError, openAi. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `970dd3c6-de83-46fd-9038-33c470571390`
- **Method**: `POST`
- **Webhook ID**: `970dd3c6-de83-46fd-9038-33c470571390`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required

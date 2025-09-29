# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 9 different services: webhook, stickyNote, switch, respondToWebhook, set. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `tool/xml-to-json`
- **Method**: `POST`
- **Webhook ID**: `add125c9-1591-4e1c-b68c-8032b99b6010`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`

## Environment Variables
- No environment variables required

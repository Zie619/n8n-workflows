# API Documentation: Weather via Slack

## Overview
Automated workflow: Weather via Slack. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `slack1`
- **Method**: `POST`
- **Webhook ID**: `41a60a4f-66d0-433b-aa43-b225dffa6761`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

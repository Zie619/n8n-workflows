# API Documentation: Zendesk Workflow

## Overview
Automated workflow: Zendesk Workflow. This workflow integrates 8 different services: webhook, stickyNote, code, set, stopAndError. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `b7845b15-0a44-4be5-b513-f4f4bb8989a6`
- **Method**: `POST`
- **Webhook ID**: `b7845b15-0a44-4be5-b513-f4f4bb8989a6`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.zendesk`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Zendesk
- Zendesk
- Slack
- Slack

## Required Credentials
- `slackOAuth2Api`
- `zendeskApi`

## Environment Variables
- No environment variables required

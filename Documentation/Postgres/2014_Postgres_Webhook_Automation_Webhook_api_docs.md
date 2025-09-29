# API Documentation: Suspicious_login_detection

## Overview
Automated workflow: Suspicious_login_detection. This workflow integrates 15 different services: webhook, stickyNote, httpRequest, code, merge. It contains 56 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 85
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `705ca4c4-0a38-4ef8-9de9-abc8b3686dc6`
- **Method**: `POST`
- **Webhook ID**: `705ca4c4-0a38-4ef8-9de9-abc8b3686dc6`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.html`
- `n8n-nodes-base.set`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.gmail`

## Integrations
- Slack

## Required Credentials
- `httpQueryAuth`
- `httpHeaderAuth`
- `gmailOAuth2`
- `slackApi`
- `postgres`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

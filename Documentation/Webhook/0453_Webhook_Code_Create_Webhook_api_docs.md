# API Documentation: Slack Workflow

## Overview
Automated workflow: Slack Workflow. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, code, merge. It contains 54 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 91
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.executeWorkflowTrigger`

### Webhook Endpoints
- **Path**: `a14585bb-b757-410e-a5b2-5f05a087b388`
- **Method**: `POST`
- **Webhook ID**: `a14585bb-b757-410e-a5b2-5f05a087b388`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack
- Slack
- Slack

## Required Credentials
- `slackApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

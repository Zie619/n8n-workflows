# API Documentation: Filter Workflow

## Overview
Automated workflow: Filter Workflow. This workflow integrates 7 different services: webhook, filter, stickyNote, clearbit, stopAndError. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `abde7a49-208b-4bce-bcb9-910c4e529b06`
- **Method**: `POST`
- **Webhook ID**: `06e900e8-9a4f-4786-bd79-928459c36e68`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.clearbit`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `clearbitApi`
- `slackApi`

## Environment Variables
- No environment variables required

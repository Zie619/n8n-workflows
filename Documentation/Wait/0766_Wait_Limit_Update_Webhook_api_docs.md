# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 13 different services: webhook, stickyNote, wait, scheduleTrigger, merge. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `f992f346-0076-4a79-a046-5b5c295bf6c2`
- **Method**: `POST`
- **Webhook ID**: `f992f346-0076-4a79-a046-5b5c295bf6c2`


## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.limit`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Slack
- Slack
- Google
- Google

## Required Credentials
- `slackOAuth2Api`
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`

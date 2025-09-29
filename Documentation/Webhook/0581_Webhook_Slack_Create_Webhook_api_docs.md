# API Documentation: Venafitlsprotectcloud Workflow

## Overview
Automated workflow: Venafitlsprotectcloud Workflow. This workflow integrates 14 different services: webhook, stickyNote, httpRequest, merge, switch. It contains 54 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 83
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `venafiendpoint`
- **Method**: `POST`
- **Webhook ID**: `4f86c00d-ceb4-4890-84c5-850f8e5dec05`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.venafiTlsProtectCloud`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack
- Slack

## Required Credentials
- `slackApi`
- `virusTotalApi`
- `openAiApi`
- `venafiTlsProtectCloudApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

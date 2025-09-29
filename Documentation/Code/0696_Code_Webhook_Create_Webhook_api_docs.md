# API Documentation: Switch Workflow

## Overview
Automated workflow: Switch Workflow. This workflow integrates 15 different services: webhook, filter, httpRequest, stickyNote, splitInBatches. It contains 67 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 96
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `a82f0ae7-678e-49d9-8219-7281e8a2a1b2`
- **Method**: `POST`
- **Webhook ID**: `a82f0ae7-678e-49d9-8219-7281e8a2a1b2`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `BASE_URL`

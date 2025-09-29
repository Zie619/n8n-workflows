# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 14 different services: webhook, filter, httpRequest, stickyNote, splitInBatches. It contains 65 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 102
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `267ea500-e2cd-4604-a31f-f0773f27317c`
- **Method**: `POST`
- **Webhook ID**: `267ea500-e2cd-4604-a31f-f0773f27317c`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
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
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`

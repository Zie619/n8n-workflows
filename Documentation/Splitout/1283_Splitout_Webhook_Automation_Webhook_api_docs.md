# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 19 different services: stickyNote, merge, lmChatOpenAi, if, chatTrigger. It contains 47 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 64
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `website-chat-example`
- **Method**: `POST`
- **Webhook ID**: `18474f2d-9472-4a8d-8e63-8128fd2cbefc`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.wooCommerce`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.dhl`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `dhlApi`
- `wooCommerceApi`

## Environment Variables
- `WEBHOOK_URL`

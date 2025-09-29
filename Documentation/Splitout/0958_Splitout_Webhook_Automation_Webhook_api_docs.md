# API Documentation: LLM Chaining examples

## Overview
Automated workflow: LLM Chaining examples. This workflow integrates 15 different services: webhook, stickyNote, httpRequest, markdown, agent. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 61
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `58d2b899-e09c-45bf-b59b-961a5d7a2470`
- **Method**: `POST`
- **Webhook ID**: `58d2b899-e09c-45bf-b59b-961a5d7a2470`


## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `anthropicApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

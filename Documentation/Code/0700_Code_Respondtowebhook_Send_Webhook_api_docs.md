# API Documentation: Memorybufferwindow Workflow

## Overview
Automated workflow: Memorybufferwindow Workflow. This workflow integrates 16 different services: microsoftOutlook, httpRequest, stickyNote, toolHttpRequest, code. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 54
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.respondToWebhook`

## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Microsoft

## Required Credentials
- `openAiApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

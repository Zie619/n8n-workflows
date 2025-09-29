# API Documentation: AI Customer-Support Assistant · WhatsApp Ready · Works for Any Business

## Overview
Automated workflow: AI Customer-Support Assistant · WhatsApp Ready · Works for Any Business. This workflow integrates 10 different services: stickyNote, code, toolHttpRequest, agent, memoryPostgresChat. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.whatsAppTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `n8n-nodes-base.whatsAppTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `whatsAppApi`
- `openAiApi`
- `whatsAppTriggerApi`
- `postgres`

## Environment Variables
- `WEBHOOK_URL`

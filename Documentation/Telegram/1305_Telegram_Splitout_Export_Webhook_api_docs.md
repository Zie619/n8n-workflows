# API Documentation: All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem

## Overview
Automated workflow: All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem. This workflow integrates 19 different services: convertToFile, stickyNote, merge, switch, lmChatOpenAi. It contains 59 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 68
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `gram`
- **Method**: `POST`
- **Webhook ID**: `097f36f3-1574-44f9-815f-58387e3b20bf`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.baserowTool`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.if`
- `n8n-nodes-base.baserow`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`
- `postgres`
- `baserowApi`

## Environment Variables
- No environment variables required

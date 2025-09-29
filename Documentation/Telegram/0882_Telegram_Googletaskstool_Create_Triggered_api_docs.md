# API Documentation: Telegramtrigger Workflow

## Overview
Automated workflow: Telegramtrigger Workflow. This workflow integrates 13 different services: telegramTrigger, stickyNote, googleTasksTool, telegram, agent. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `n8n-nodes-base.set`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.googleTasksTool`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `openAiApi`
- `telegramApi`
- `googleTasksOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`

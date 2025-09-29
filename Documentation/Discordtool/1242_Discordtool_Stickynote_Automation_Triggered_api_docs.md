# API Documentation: Discord Agent

## Overview
Automated workflow: Discord Agent. This workflow integrates 8 different services: stickyNote, agent, discordTool, stopAndError, lmChatOpenAi. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.discordTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `discordBotApi`

## Environment Variables
- `WEBHOOK_URL`

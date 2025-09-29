# API Documentation: Discord MCP Chat Agent

## Overview
Automated workflow: Discord MCP Chat Agent. This workflow integrates 6 different services: stickyNote, agent, mcpClientTool, stopAndError, lmChatOpenAi. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 13
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`

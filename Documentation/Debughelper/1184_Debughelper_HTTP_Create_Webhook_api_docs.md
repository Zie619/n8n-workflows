# API Documentation: Build your first AI MCP Server

## Overview
Automated workflow: Build your first AI MCP Server. This workflow integrates 15 different services: stickyNote, httpRequest, agent, mcpClientTool, switch. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 48
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.debugHelper`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

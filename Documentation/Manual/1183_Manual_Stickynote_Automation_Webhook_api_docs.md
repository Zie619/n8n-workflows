# API Documentation: Enhance Chat Responses with Real-Time Search Data via Bright Data & Gemini AI

## Overview
Automated workflow: Enhance Chat Responses with Real-Time Search Data via Bright Data & Gemini AI. This workflow integrates 11 different services: stickyNote, toolHttpRequest, lmChatGoogleGemini, agent, mcpClientTool. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-mcp.mcpClientTool`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `n8n-nodes-mcp.mcpClient`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `mcpClientApi`

## Environment Variables
- `WEBHOOK_URL`

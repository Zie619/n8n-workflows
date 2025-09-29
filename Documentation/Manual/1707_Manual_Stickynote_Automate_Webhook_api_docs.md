# API Documentation: Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent

## Overview
Automated workflow: Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent. This workflow integrates 12 different services: stickyNote, httpRequest, lmChatGoogleGemini, agent, mcpClientTool. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.function`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-mcp.mcpClient`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-mcp.mcpClientTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `mcpClientApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

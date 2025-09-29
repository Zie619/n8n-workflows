# API Documentation: Discord MCP Server

## Overview
Automated workflow: Discord MCP Server. This workflow integrates 5 different services: stickyNote, mcpTrigger, stopAndError, discordTool, httpRequestTool. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequestTool`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.discordTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `discordBotApi`

## Environment Variables
- `API_BASE_URL`

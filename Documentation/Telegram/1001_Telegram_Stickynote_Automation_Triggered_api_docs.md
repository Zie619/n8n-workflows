# API Documentation: MCP Client with Brave and Telegram

## Overview
Automated workflow: MCP Client with Brave and Telegram. This workflow integrates 8 different services: telegramTrigger, stickyNote, telegram, code, set. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.code`
- `n8n-nodes-mcp.mcpClient`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `mcpClientApi`

## Environment Variables
- No environment variables required

# API Documentation: Personal Assistant MCP server

## Overview
Automated workflow: Personal Assistant MCP server. This workflow integrates 11 different services: stickyNote, lmChatGoogleGemini, gmailTool, mcpClientTool, agent. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.googleSheetsTool`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.googleCalendarTool`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googleCalendarOAuth2Api`
- `googlePalmApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `API_ENDPOINT`

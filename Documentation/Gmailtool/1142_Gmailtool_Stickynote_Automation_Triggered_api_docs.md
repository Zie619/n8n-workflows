# API Documentation: DeepSeek v3.1

## Overview
Automated workflow: DeepSeek v3.1. This workflow integrates 8 different services: notionTrigger, stickyNote, gmailTool, agent, mcpClientTool. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.notionTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notionTrigger`
- `n8n-nodes-base.wordpressTool`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-mcp.mcpClientTool`

## Integrations
- No external integrations detected

## Required Credentials
- `deepSeekApi`
- `mcpClientApi`
- `notionApi`
- `gmailOAuth2`
- `wordpressApi`

## Environment Variables
- No environment variables required

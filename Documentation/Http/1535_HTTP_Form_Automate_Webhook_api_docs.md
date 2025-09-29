# API Documentation: 💥🛠️Automate Blog Content Creation with GPT-4, Perplexity & WordPress

## Overview
Automated workflow: 💥🛠️Automate Blog Content Creation with GPT-4, Perplexity & WordPress. This workflow integrates 11 different services: stickyNote, httpRequest, formTrigger, gmailTool, agent. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.wordpressTool`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-mcp.mcpClientTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `mcpClientApi`
- `gmailOAuth2`
- `wordpressApi`

## Environment Variables
- `API_BASE_URL`

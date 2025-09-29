# API Documentation: MCP_SUPABASE_AGENT

## Overview
Automated workflow: MCP_SUPABASE_AGENT. This workflow integrates 6 different services: stickyNote, supabaseTool, mcpTrigger, stopAndError, embeddingsOpenAi. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.supabaseTool`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `supabaseApi`

## Environment Variables
- No environment variables required

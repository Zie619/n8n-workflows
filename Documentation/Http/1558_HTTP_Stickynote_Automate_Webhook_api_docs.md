# API Documentation: ✨📊Multi-AI Agent Chatbot for Postgres/Supabase DB and QuickCharts + Tool Router

## Overview
Automated workflow: ✨📊Multi-AI Agent Chatbot for Postgres/Supabase DB and QuickCharts + Tool Router. This workflow integrates 13 different services: postgresTool, stickyNote, httpRequest, agent, outputParserStructured. It contains 45 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 54
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.postgresTool`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `postgres`

## Environment Variables
- `BASE_URL`

# API Documentation: OpenAI Assistant with custom n8n tools

## Overview
Automated workflow: OpenAI Assistant with custom n8n tools. This workflow integrates 12 different services: stickyNote, openAiAssistant, code, merge, summarize. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.manualChatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.toolCode`
- `@n8n/n8n-nodes-langchain.manualChatTrigger`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.code`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.openAiAssistant`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required

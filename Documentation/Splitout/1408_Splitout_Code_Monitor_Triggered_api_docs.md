# API Documentation: Code Workflow

## Overview
Automated workflow: Code Workflow. This workflow integrates 12 different services: filter, stickyNote, code, lmOllama, splitOut. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.lmOllama`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `ollamaApi`

## Environment Variables
- No environment variables required

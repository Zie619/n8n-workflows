# API Documentation: Executeworkflowtrigger Workflow

## Overview
Automated workflow: Executeworkflowtrigger Workflow. This workflow integrates 12 different services: stickyNote, httpRequest, filter, switch, set. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.set`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

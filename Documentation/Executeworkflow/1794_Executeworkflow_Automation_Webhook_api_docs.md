# API Documentation: 🤖Content Creator Agent

## Overview
Automated workflow: 🤖Content Creator Agent. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `anthropicApi`

## Environment Variables
- `API_BASE_URL`

# API Documentation: Memorybufferwindow Workflow

## Overview
Automated workflow: Memorybufferwindow Workflow. This workflow integrates 18 different services: stickyNote, httpRequest, formTrigger, code, scheduleTrigger. It contains 62 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 95
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.toolThink`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `smtp`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

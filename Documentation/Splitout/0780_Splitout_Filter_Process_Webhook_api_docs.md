# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 19 different services: stickyNote, airtable, merge, outputParserAutofixing, executeWorkflow. It contains 63 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 92
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `n8n-nodes-base.html`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `openRouterApi`
- `anthropicApi`
- `httpHeaderAuth`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

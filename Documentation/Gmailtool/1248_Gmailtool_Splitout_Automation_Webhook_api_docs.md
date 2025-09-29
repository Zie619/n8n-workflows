# API Documentation: Agent Workflow

## Overview
Automated workflow: Agent Workflow. This workflow integrates 12 different services: webhook, stickyNote, httpRequest, airtable, gmailTool. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `df852a9f-5ea3-43f2-bd49-d045aba5e9c9`
- **Method**: `POST`
- **Webhook ID**: `df852a9f-5ea3-43f2-bd49-d045aba5e9c9`


## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`
- `gmailOAuth2`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

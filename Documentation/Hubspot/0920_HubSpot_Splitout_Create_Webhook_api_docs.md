# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 18 different services: webhook, stickyNote, httpRequest, filter, markdown. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 55
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.hubspotTrigger`

### Webhook Endpoints
- **Path**: `06d29616-8fa9-42cf-8b5f-abe856083c75`
- **Method**: `POST`
- **Webhook ID**: `06d29616-8fa9-42cf-8b5f-abe856083c75`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.hubspotTrigger`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Hubspot
- Hubspot
- Hubspot

## Required Credentials
- `hubspotDeveloperApi`
- `openAiApi`
- `googleCalendarOAuth2Api`
- `gmailOAuth2`
- `hubspotOAuth2Api`

## Environment Variables
- `API_BASE_URL`

# API Documentation: Gmail Workflow

## Overview
Automated workflow: Gmail Workflow. This workflow integrates 19 different services: stickyNote, scheduleTrigger, merge, switch, lmChatOpenAi. It contains 68 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 77
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.html`
- `n8n-nodes-base.executeWorkflow`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`
- `httpQueryAuth`
- `gmailOAuth2`
- `whatsAppApi`

## Environment Variables
- `API_BASE_URL`

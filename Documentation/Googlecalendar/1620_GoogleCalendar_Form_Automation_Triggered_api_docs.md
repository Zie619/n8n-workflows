# API Documentation: Formtrigger Workflow

## Overview
Automated workflow: Formtrigger Workflow. This workflow integrates 13 different services: textClassifier, stickyNote, formTrigger, chainLlm, set. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleCalendar`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.form`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

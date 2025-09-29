# API Documentation: Zoom AI Meeting Assistant

## Overview
Automated workflow: Zoom AI Meeting Assistant. This workflow integrates 19 different services: stickyNote, toolThink, emailSend, extractFromFile, splitInBatches. It contains 30 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 51
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.code`
- `n8n-nodes-base.clickUp`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.zoom`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.microsoftOutlookTool`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.toolThink`
- `n8n-nodes-base.set`

## Integrations
- Microsoft

## Required Credentials
- `anthropicApi`
- `smtp`
- `zoomOAuth2Api`
- `microsoftOutlookOAuth2Api`
- `clickUpOAuth2Api`

## Environment Variables
- `BASE_URL`

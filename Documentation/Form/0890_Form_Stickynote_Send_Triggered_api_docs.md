# API Documentation: Hubspot Workflow

## Overview
Automated workflow: Hubspot Workflow. This workflow integrates 10 different services: stickyNote, formTrigger, hubspot, gmailTool, agent. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.form`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Hubspot
- Hubspot

## Required Credentials
- `hubspotOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

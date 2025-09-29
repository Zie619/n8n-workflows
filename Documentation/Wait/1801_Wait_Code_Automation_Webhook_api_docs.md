# API Documentation: spy tool

## Overview
Automated workflow: spy tool. This workflow integrates 9 different services: stickyNote, httpRequest, formTrigger, wait, code. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `httpBasicAuth`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`

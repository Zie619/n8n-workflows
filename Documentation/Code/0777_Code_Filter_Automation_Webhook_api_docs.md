# API Documentation: mails2notion V2

## Overview
Automated workflow: mails2notion V2. This workflow integrates 15 different services: filter, httpRequest, stickyNote, airtable, code. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 51
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `gmailOAuth2`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

# API Documentation: Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API

## Overview
Automated workflow: Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API. This workflow integrates 11 different services: stickyNote, httpRequest, airtable, code, scheduleTrigger. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.airtableTool`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `gmailOAuth2`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

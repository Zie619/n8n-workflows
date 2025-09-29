# API Documentation: Twiliotrigger Workflow

## Overview
Automated workflow: Twiliotrigger Workflow. This workflow integrates 13 different services: stickyNote, airtable, toolHttpRequest, scheduleTrigger, agent. It contains 51 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 80
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.twilioTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.twilioTrigger`
- `n8n-nodes-base.twilio`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `calApi`
- `openAiApi`
- `httpHeaderAuth`
- `twilioApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

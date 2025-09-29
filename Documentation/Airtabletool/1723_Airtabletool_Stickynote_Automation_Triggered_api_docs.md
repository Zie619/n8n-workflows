# API Documentation: AI Social Media Caption Creator

## Overview
Automated workflow: AI Social Media Caption Creator. This workflow integrates 10 different services: airtableTrigger, stickyNote, wait, airtable, agent. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.airtableTrigger`

## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.airtableTool`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`

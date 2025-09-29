# API Documentation: AI Logo Sheet Extractor to Airtable

## Overview
Automated workflow: AI Logo Sheet Extractor to Airtable. This workflow integrates 15 different services: stickyNote, formTrigger, airtable, code, agent. It contains 45 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 50
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`

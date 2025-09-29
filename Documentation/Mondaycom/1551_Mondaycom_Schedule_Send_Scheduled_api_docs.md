# API Documentation: Microsoft Outlook AI Email Assistant

## Overview
Automated workflow: Microsoft Outlook AI Email Assistant. This workflow integrates 15 different services: microsoftOutlook, stickyNote, markdown, airtable, scheduleTrigger. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.mondayCom`

## Integrations
- Microsoft
- Microsoft
- Microsoft

## Required Credentials
- `openAiApi`
- `mondayComApi`
- `airtableTokenApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`

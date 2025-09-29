# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 13 different services: stickyNote, splitInBatches, toolSerpApi, scheduleTrigger, agent. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.toolSerpApi`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `serpApi`
- `openAiApi`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

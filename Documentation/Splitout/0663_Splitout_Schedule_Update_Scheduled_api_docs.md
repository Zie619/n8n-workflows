# API Documentation: Splitout Workflow

## Overview
Automated workflow: Splitout Workflow. This workflow integrates 14 different services: airtableTrigger, stickyNote, airtable, scheduleTrigger, splitOut. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.airtableTrigger`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.graphql`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `httpHeaderAuth`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

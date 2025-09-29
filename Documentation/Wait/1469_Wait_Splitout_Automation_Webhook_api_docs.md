# API Documentation: Content to 9:16 Aspect Image Generator v1

## Overview
Automated workflow: Content to 9:16 Aspect Image Generator v1. This workflow integrates 14 different services: stickyNote, filter, httpRequest, wait, airtable. It contains 52 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 81
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.limit`
- `@n8n/n8n-nodes-langchain.toolWikipedia`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpCustomAuth`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

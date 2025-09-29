# API Documentation: Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool

## Overview
Automated workflow: Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, markdown, splitInBatches. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `53166f88-c88a-4429-b6b5-498f458686b0`
- **Method**: `POST`
- **Webhook ID**: ``


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleApi`
- `openAiApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

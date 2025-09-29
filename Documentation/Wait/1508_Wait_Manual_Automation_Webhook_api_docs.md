# API Documentation: Indeed Company Data Scraper & Summarization with Airtable, Bright Data and Google Gemini

## Overview
Automated workflow: Indeed Company Data Scraper & Summarization with Airtable, Bright Data and Google Gemini. This workflow integrates 15 different services: stickyNote, httpRequest, markdown, wait, airtable. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
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
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googlePalmApi`
- `httpHeaderAuth`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

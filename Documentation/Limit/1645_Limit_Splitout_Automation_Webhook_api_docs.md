# API Documentation: Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI

## Overview
Automated workflow: Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI. This workflow integrates 13 different services: stickyNote, httpRequest, splitOut, informationExtractor, set. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.sentimentAnalysis`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

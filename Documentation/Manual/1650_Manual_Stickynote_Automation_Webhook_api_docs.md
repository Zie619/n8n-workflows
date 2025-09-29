# API Documentation: Search & Summarize Web Data with Perplexity, Gemini AI & Bright Data to Webhooks

## Overview
Automated workflow: Search & Summarize Web Data with Perplexity, Gemini AI & Bright Data to Webhooks. This workflow integrates 12 different services: stickyNote, httpRequest, wait, textSplitterRecursiveCharacterTextSplitter, lmChatGoogleGemini. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 48
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google

## Required Credentials
- `googlePalmApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

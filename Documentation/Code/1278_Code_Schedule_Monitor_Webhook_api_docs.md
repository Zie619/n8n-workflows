# API Documentation: AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack

## Overview
Automated workflow: AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack. This workflow integrates 14 different services: textClassifier, stickyNote, httpRequest, code, scheduleTrigger. It contains 40 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Slack
- Google
- Google
- Google

## Required Credentials
- `slackOAuth2Api`
- `googleApi`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

# API Documentation: Analyze Reddit Posts with AI to Identify Business Opportunities

## Overview
Automated workflow: Analyze Reddit Posts with AI to Identify Business Opportunities. This workflow integrates 14 different services: stickyNote, agent, merge, reddit, set. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.sentimentAnalysis`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.reddit`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `redditOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

# API Documentation: 📄✨ Easy Wordpress Content Creation from PDF Document + Human In The Loop with Gmail Approval

## Overview
Automated workflow: 📄✨ Easy Wordpress Content Creation from PDF Document + Human In The Loop with Gmail Approval. This workflow integrates 14 different services: stickyNote, formTrigger, httpRequest, wordpress, telegram. It contains 40 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 61
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`
- `wordpressApi`
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

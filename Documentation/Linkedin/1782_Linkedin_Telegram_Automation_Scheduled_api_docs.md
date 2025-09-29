# API Documentation: Social Media AI Agent - Telegram

## Overview
Automated workflow: Social Media AI Agent - Telegram. This workflow integrates 15 different services: filter, markdown, httpRequest, stickyNote, airtable. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.linkedIn`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `linkedInOAuth2Api`
- `twitterOAuth2Api`
- `telegramApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

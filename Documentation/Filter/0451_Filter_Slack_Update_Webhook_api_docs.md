# API Documentation: Lineartrigger Workflow

## Overview
Automated workflow: Lineartrigger Workflow. This workflow integrates 11 different services: filter, httpRequest, stickyNote, linearTrigger, merge. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.linearTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.linear`
- `n8n-nodes-base.linearTrigger`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `linearOAuth2Api`
- `linearApi`

## Environment Variables
- `API_BASE_URL`

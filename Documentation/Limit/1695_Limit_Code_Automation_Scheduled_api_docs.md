# API Documentation: Github Releases

## Overview
Automated workflow: Github Releases. This workflow integrates 14 different services: stickyNote, code, scheduleTrigger, lmChatGoogleGemini, set. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.redis`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Slack
- Slack
- Google

## Required Credentials
- `slackApi`
- `googlePalmApi`
- `redis`

## Environment Variables
- `BASE_URL`

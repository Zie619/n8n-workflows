# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 13 different services: stickyNote, filter, code, scheduleTrigger, merge. It contains 30 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.webflow`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackOAuth2Api`
- `webflowOAuth2Api`
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`

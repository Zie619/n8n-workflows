# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 9 different services: mongoDb, httpRequest, stickyNote, scheduleTrigger, merge. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.mongoDb`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `httpQueryAuth`
- `mongoDb`

## Environment Variables
- `BASE_URL`

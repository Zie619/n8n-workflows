# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 11 different services: filter, stickyNote, code, scheduleTrigger, trello. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.trello`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `trelloApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

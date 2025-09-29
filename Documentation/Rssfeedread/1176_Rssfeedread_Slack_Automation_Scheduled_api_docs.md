# API Documentation: Post RSS feed items from yesterday to Slack

## Overview
Automated workflow: Post RSS feed items from yesterday to Slack. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.function`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.if`

## Integrations
- Slack

## Required Credentials
- `slackApi`

## Environment Variables
- `WEBHOOK_URL`

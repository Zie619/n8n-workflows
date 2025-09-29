# API Documentation: Scrape Twitter for mentions of company

## Overview
Automated workflow: Scrape Twitter for mentions of company. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `twitterOAuth1Api`

## Environment Variables
- No environment variables required

# API Documentation: ETL pipeline

## Overview
Automated workflow: ETL pipeline. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.if`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.googleCloudNaturalLanguage`
- `n8n-nodes-base.set`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.mongoDb`

## Integrations
- Slack
- Google

## Required Credentials
- `twitterOAuth1Api`
- `postgres`
- `slackApi`
- `googleCloudNaturalLanguageOAuth2Api`
- `mongoDb`

## Environment Variables
- No environment variables required

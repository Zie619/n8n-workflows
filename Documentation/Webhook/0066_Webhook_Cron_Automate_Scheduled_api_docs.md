# API Documentation: Standup Bot - Worker

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.cron`

### Webhook Endpoints
- **Path**: `standup-bot/action/f6f9b174745fa4651f750c36957d674c`
- **Method**: `POST`
- **Webhook ID**: `6a28d86b-9f74-4825-9785-57e0d43b198f`

- **Path**: `standup-bot/slashCmd`
- **Method**: `POST`
- **Webhook ID**: `72732516-1143-430f-8465-d193fe657311`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.function`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.mattermost`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`

## Integrations
- No external integrations detected

## Required Credentials
- `mattermostApi`

## Environment Variables
- `BASE_URL`

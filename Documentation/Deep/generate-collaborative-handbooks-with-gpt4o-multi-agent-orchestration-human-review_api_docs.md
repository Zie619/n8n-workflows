# API Documentation: Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `pyragogy/process`
- **Method**: `POST`
- **Webhook ID**: `pyragogy-master-trigger`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.github`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.if`
- `n8n-nodes-base.function`
- `n8n-nodes-base.start`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.wait`

## Integrations
- Github
- Slack

## Required Credentials
- `openAiApi`
- `postgres`
- `emailSend`
- `githubApi`

## Environment Variables
- `BASE_URL`

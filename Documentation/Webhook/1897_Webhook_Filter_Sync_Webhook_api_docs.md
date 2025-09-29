# API Documentation: Realtime Notion Todoist 2-way Sync Template

## Overview
Automated workflow: Realtime Notion Todoist 2-way Sync Template. This workflow integrates 29 different services: stickyNote, scheduleTrigger, merge, switch, redis. It contains 264 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 341
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `7aee8b09-29e3-4e12-9b66-c6e8ab080bf7`
- **Method**: `['GET']`
- **Webhook ID**: `7aee8b09-29e3-4e12-9b66-c6e8ab080bf7`

- **Path**: `7e1a4d8a-9cdc-4991-817c-1429ccfbece2`
- **Method**: `POST`
- **Webhook ID**: `7e1a4d8a-9cdc-4991-817c-1429ccfbece2`

- **Path**: `47b150f3-12a3-4fe9-97cc-5d139daa3b00`
- **Method**: `POST`
- **Webhook ID**: `81107d16-d839-4507-a627-f607f1d53d4e`

- **Path**: `1d758ef5-a9b9-4313-b81e-1c7dfe230a33`
- **Method**: `POST`
- **Webhook ID**: `1d758ef5-a9b9-4313-b81e-1c7dfe230a33`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.form`
- `n8n-nodes-base.code`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.executionData`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.html`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.if`
- `n8n-nodes-base.todoist`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`
- `notionApi`
- `redis`
- `todoistApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

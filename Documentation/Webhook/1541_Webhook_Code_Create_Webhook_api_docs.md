# API Documentation: Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened

## Overview
Automated workflow: Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened. This workflow integrates 9 different services: webhook, stickyNote, httpRequest, code, noOp. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `3ea0b887-9caa-477e-b6e4-1d3edf72d11e`
- **Method**: `POST`
- **Webhook ID**: `3ea0b887-9caa-477e-b6e4-1d3edf72d11e`


## Node Types Used
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `jiraSoftwareCloudApi`
- `slackApi`
- `httpHeaderAuth`
- `slackOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

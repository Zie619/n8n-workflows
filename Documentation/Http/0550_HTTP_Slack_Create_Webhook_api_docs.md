# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 6 different services: webhook, stickyNote, httpRequest, set, stopAndError. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `833df60e-a78f-4a59-8244-9694f27cf8ae`
- **Method**: `POST`
- **Webhook ID**: `833df60e-a78f-4a59-8244-9694f27cf8ae`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `hubspotOAuth2Api`
- `slackApi`
- `hubspotAppToken`

## Environment Variables
- `API_BASE_URL`

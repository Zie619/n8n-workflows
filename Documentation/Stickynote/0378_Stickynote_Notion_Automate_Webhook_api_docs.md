# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 4 different services: webhook, stickyNote, stopAndError, notion. It contains 6 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `1c04b027-39d2-491a-a9c6-194289fe400c`
- **Method**: `POST`
- **Webhook ID**: `0626e4cc-e132-4024-9ab9-443a9ac7b133`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`

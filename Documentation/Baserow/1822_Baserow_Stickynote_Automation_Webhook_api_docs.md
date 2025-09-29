# API Documentation: Baserow markdown to html

## Overview
Automated workflow: Baserow markdown to html. This workflow integrates 6 different services: webhook, stickyNote, markdown, stopAndError, baserow. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `d4858ac8-2d80-41c5-a9d9-06b8e1a14347`
- **Method**: `POST`
- **Webhook ID**: `d4858ac8-2d80-41c5-a9d9-06b8e1a14347`


## Node Types Used
- `n8n-nodes-base.baserow`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `baserowApi`

## Environment Variables
- No environment variables required

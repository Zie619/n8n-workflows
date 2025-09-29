# API Documentation: Mysql Workflow

## Overview
Automated workflow: Mysql Workflow. This workflow integrates 6 different services: webhook, stickyNote, httpRequest, mySql, code. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `pr-notify-template`
- **Method**: `POST`
- **Webhook ID**: `05a0f565-7a1e-44f2-956d-1c68982ce314`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.mySql`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `mySql`

## Environment Variables
- `API_BASE_URL`

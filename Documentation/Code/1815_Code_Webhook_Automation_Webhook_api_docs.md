# API Documentation: puq-docker-influxdb-deploy

## Overview
Automated workflow: puq-docker-influxdb-deploy. This workflow integrates 9 different services: webhook, stickyNote, code, switch, set. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 56
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `docker-influxdb`
- **Method**: `['POST']`
- **Webhook ID**: `6760feea-1d9b-466c-82a9-3891a300b0fd`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.ssh`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpBasicAuth`
- `sshPassword`

## Environment Variables
- No environment variables required

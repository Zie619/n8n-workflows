# API Documentation: Find Top Keywords

## Overview
Automated workflow: Find Top Keywords. This workflow integrates 11 different services: stickyNote, httpRequest, filter, code, scheduleTrigger. It contains 51 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 88
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.nocoDb`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `nocoDbApiToken`
- `httpHeaderAuth`
- `httpBasicAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

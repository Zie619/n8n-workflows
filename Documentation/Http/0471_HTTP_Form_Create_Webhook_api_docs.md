# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 6 different services: stickyNote, httpRequest, formTrigger, respondToWebhook, set. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.respondToWebhook`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `stripeApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

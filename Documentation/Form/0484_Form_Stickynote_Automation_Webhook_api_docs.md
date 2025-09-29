# API Documentation: Dynamic credentials using expressions

## Overview
Automated workflow: Dynamic credentials using expressions. This workflow integrates 5 different services: stickyNote, formTrigger, respondToWebhook, stopAndError, nasa. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.respondToWebhook`

## Node Types Used
- `n8n-nodes-base.nasa`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `nasaApi`

## Environment Variables
- `BASE_URL`

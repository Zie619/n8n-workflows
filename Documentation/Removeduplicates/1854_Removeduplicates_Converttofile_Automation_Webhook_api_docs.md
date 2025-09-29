# API Documentation: Query List of Sign-in IPs

## Overview
Automated workflow: Query List of Sign-in IPs. This workflow integrates 9 different services: convertToFile, stickyNote, httpRequest, formTrigger, merge. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.moveBinaryData`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

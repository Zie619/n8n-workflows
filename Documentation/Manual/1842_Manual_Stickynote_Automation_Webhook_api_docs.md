# API Documentation: Merge

## Overview
Automated workflow: Merge. This workflow integrates 5 different services: stickyNote, httpRequest, readWriteFile, stopAndError, manualTrigger. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpQueryAuth`

## Environment Variables
- `API_BASE_URL`

# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 10 different services: stickyNote, filter, scheduleTrigger, dropbox, n8n. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.moveBinaryData`
- `n8n-nodes-base.if`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.dropbox`
- `n8n-nodes-base.n8n`

## Integrations
- No external integrations detected

## Required Credentials
- `dropboxOAuth2Api`
- `n8nApi`

## Environment Variables
- No environment variables required

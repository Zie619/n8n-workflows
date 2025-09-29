# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 5 different services: stickyNote, itemLists, filter, scheduleTrigger, gmail. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- No environment variables required

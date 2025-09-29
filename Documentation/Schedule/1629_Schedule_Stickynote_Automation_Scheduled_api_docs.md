# API Documentation: Reschedule overdue Asana tasks and clean up completed tasks

## Overview
Automated workflow: Reschedule overdue Asana tasks and clean up completed tasks. This workflow integrates 4 different services: scheduleTrigger, asana, stickyNote, if. It contains 10 nodes and follows best practices for error handling and security.

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
- `n8n-nodes-base.if`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.asana`

## Integrations
- No external integrations detected

## Required Credentials
- `asanaApi`

## Environment Variables
- No environment variables required

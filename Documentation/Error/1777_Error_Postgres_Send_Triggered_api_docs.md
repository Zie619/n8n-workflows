# API Documentation: Log errors and avoid sending too many emails

## Overview
Automated workflow: Log errors and avoid sending too many emails. This workflow integrates 12 different services: postgres, stickyNote, code, errorTrigger, pushover. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.if`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.pushover`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `pushoverApi`
- `postgres`
- `smtp`

## Environment Variables
- `BASE_URL`

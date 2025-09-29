# API Documentation: Addon for Workflow Nodes Update Check Template

## Overview
Automated workflow: Addon for Workflow Nodes Update Check Template. This workflow integrates 7 different services: stickyNote, code, n8n, set, gmail. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

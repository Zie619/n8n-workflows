# API Documentation: Email form

## Overview
Automated workflow: Email form. This workflow integrates 6 different services: stickyNote, hunter, formTrigger, if, noOp. It contains 7 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sendGrid`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`

## Integrations
- No external integrations detected

## Required Credentials
- `hunterApi`
- `sendGridApi`

## Environment Variables
- No environment variables required

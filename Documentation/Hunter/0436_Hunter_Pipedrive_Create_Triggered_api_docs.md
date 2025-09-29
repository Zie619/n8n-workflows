# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 7 different services: pipedrive, stickyNote, hunter, formTrigger, clearbit. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.clearbit`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`
- `n8n-nodes-base.pipedrive`

## Integrations
- No external integrations detected

## Required Credentials
- `hunterApi`
- `pipedriveApi`
- `clearbitApi`

## Environment Variables
- No environment variables required

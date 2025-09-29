# API Documentation: Errortrigger Workflow

## Overview
Automated workflow: Errortrigger Workflow. This workflow integrates 7 different services: stickyNote, code, scheduleTrigger, n8n, errorTrigger. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.if`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

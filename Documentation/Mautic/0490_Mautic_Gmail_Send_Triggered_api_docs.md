# API Documentation: Unsubscribe Mautic contacts from automated unsubscribe emails

## Overview
Automated workflow: Unsubscribe Mautic contacts from automated unsubscribe emails. This workflow integrates 7 different services: stickyNote, mautic, code, gmailTrigger, set. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.mautic`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `mauticOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

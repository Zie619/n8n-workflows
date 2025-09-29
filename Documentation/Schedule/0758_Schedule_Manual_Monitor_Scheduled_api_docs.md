# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 9 different services: stickyNote, salesforce, scheduleTrigger, set, sort. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.salesforce`
- `n8n-nodes-base.gong`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`

## Integrations
- Salesforce

## Required Credentials
- `salesforceOAuth2Api`
- `gongApi`

## Environment Variables
- No environment variables required

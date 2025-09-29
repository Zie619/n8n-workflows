# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 15 different services: stickyNote, executionData, code, scheduleTrigger, n8n. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.executionData`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `discordBotApi`
- `n8nApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

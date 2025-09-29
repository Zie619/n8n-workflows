# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 9 different services: stickyNote, scheduleTrigger, splitOut, noOp, set. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`

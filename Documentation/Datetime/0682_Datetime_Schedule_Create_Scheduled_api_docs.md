# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 10 different services: stickyNote, scheduleTrigger, noOp, sort, stopAndError. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.serviceNow`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack

## Required Credentials
- `serviceNowBasicApi`
- `slackApi`

## Environment Variables
- No environment variables required

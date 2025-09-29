# API Documentation: Slack Workflow

## Overview
Automated workflow: Slack Workflow. This workflow integrates 8 different services: stickyNote, formTrigger, httpRequest, hunter, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `httpHeaderAuth`
- `hunterApi`

## Environment Variables
- `BASE_URL`

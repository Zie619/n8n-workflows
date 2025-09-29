# API Documentation: Linear Project Status and End Date to Productboard feature Sync

## Overview
Automated workflow: Linear Project Status and End Date to Productboard feature Sync. This workflow integrates 10 different services: stickyNote, httpRequest, code, splitOut, linearTrigger. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.linearTrigger`
- `n8n-nodes-base.linearTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.linearTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `httpHeaderAuth`
- `linearApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

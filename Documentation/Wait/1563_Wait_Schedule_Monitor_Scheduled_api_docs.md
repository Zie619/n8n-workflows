# API Documentation: PG&E Daily Cost Tracker

## Overview
Automated workflow: PG&E Daily Cost Tracker. This workflow integrates 6 different services: stickyNote, wait, scheduleTrigger, set, airtop. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.airtop`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`

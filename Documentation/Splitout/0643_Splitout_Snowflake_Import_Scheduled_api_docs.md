# API Documentation: Import Productboard Notes, Companies and Features into Snowflake

## Overview
Automated workflow: Import Productboard Notes, Companies and Features into Snowflake. This workflow integrates 9 different services: stickyNote, httpRequest, scheduleTrigger, splitOut, set. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 59
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.snowflake`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `httpHeaderAuth`
- `snowflake`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

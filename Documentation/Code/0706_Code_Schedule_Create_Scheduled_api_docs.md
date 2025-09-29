# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 11 different services: stickyNote, httpRequest, code, scheduleTrigger, function. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 68
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.function`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

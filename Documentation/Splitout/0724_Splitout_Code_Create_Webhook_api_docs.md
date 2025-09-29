# API Documentation: Notiontrigger Workflow

## Overview
Automated workflow: Notiontrigger Workflow. This workflow integrates 7 different services: notionTrigger, stickyNote, httpRequest, code, splitOut. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.notionTrigger`

## Node Types Used
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notionTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

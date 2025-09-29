# API Documentation: Read sitemap and filter URLs

## Overview
Automated workflow: Read sitemap and filter URLs. This workflow integrates 8 different services: filter, httpRequest, stickyNote, splitOut, set. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

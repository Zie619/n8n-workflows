# API Documentation: Noop Workflow

## Overview
Automated workflow: Noop Workflow. This workflow integrates 8 different services: stickyNote, httpRequest, hubspot, set, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.hubspotTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.hubspotTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Hubspot
- Hubspot
- Hubspot

## Required Credentials
- `hubspotDeveloperApi`
- `hubspotOAuth2Api`
- `httpHeaderAuth`

## Environment Variables
- `API_BASE_URL`

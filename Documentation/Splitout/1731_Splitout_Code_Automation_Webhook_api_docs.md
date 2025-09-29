# API Documentation: [2/3] Set up medoids (2 types) for anomaly detection (crops dataset)

## Overview
Automated workflow: [2/3] Set up medoids (2 types) for anomaly detection (crops dataset). This workflow integrates 8 different services: stickyNote, httpRequest, code, splitOut, merge. It contains 72 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 125
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `qdrantApi`
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

# API Documentation: [n8n] - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices

## Overview
Automated workflow: [n8n] - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices. This workflow integrates 12 different services: shopify, stickyNote, httpRequest, filter, code. It contains 61 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 110
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.shopify`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `shopifyAccessTokenApi`
- `httpHeaderAuth`
- `oAuth2Api`

## Environment Variables
- `BASE_URL`

# API Documentation: Stripe Payment Order Sync – Auto Retrieve Customer & Product Purchased

## Overview
Automated workflow: Stripe Payment Order Sync – Auto Retrieve Customer & Product Purchased. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.stripeTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stripeTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Stripe

## Required Credentials
- `httpHeaderAuth`
- `stripeApi`

## Environment Variables
- `BASE_URL`

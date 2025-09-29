# API Documentation: Shopify + Mautic

## Overview
Automated workflow: Shopify + Mautic. This workflow integrates 10 different services: webhook, stickyNote, mautic, graphql, set. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.shopifyTrigger`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `6485fca6-c641-4067-b19a-192709b88e45`
- **Method**: `POST`
- **Webhook ID**: `6485fca6-c641-4067-b19a-192709b88e45`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.shopifyTrigger`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.mautic`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.graphql`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `mauticOAuth2Api`
- `shopifyAccessTokenApi`
- `httpHeaderAuth`

## Environment Variables
- `API_ENDPOINT`

# API Documentation: Shopify order UTM to Baserow

## Overview
Automated workflow: Shopify order UTM to Baserow. This workflow integrates 8 different services: stickyNote, scheduleTrigger, graphql, splitOut, set. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.baserow`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.graphql`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`
- `baserowApi`

## Environment Variables
- `API_ENDPOINT`

# API Documentation: Weekly_Shodan_Query___Report_Accidents__no_function_node_

## Overview
Automated workflow: Weekly_Shodan_Query___Report_Accidents__no_function_node_. This workflow integrates 11 different services: itemLists, httpRequest, filter, markdown, stickyNote. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
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
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.html`
- `n8n-nodes-base.theHive`
- `n8n-nodes-base.set`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpQueryAuth`
- `theHiveApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

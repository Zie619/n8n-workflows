# API Documentation: Google Maps Email Scraper Template

## Overview
Automated workflow: Google Maps Email Scraper Template. This workflow integrates 14 different services: filter, httpRequest, stickyNote, wait, code. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`

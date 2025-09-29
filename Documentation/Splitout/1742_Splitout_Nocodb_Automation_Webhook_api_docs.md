# API Documentation: Simple LinkedIn profile collector

## Overview
Automated workflow: Simple LinkedIn profile collector. This workflow integrates 10 different services: convertToFile, stickyNote, httpRequest, splitOut, merge. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
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
- `n8n-nodes-base.nocoDb`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `serpApi`
- `openAiApi`
- `nocoDbApiToken`

## Environment Variables
- `API_BASE_URL`

# API Documentation: Prepare CSV files with GPT-4

## Overview
Automated workflow: Prepare CSV files with GPT-4. This workflow integrates 10 different services: writeBinaryFile, stickyNote, itemLists, spreadsheetFile, set. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.writeBinaryFile`
- `n8n-nodes-base.moveBinaryData`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.spreadsheetFile`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required

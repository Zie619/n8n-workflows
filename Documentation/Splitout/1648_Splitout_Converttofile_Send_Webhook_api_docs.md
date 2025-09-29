# API Documentation: Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV

## Overview
Automated workflow: Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV. This workflow integrates 9 different services: convertToFile, stickyNote, httpRequest, googleSheetsTrigger, splitOut. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.html`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `httpHeaderAuth`
- `googleSheetsTriggerOAuth2Api`
- `httpBasicAuth`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`

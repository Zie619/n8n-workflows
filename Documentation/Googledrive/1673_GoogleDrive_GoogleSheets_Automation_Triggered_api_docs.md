# API Documentation: Google Doc Summarizer to Google Sheets

## Overview
Automated workflow: Google Doc Summarizer to Google Sheets. This workflow integrates 8 different services: stickyNote, googleDriveTrigger, stopAndError, toolWikipedia, googleSheets. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleApi`
- `openAiApi`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

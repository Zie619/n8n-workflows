# API Documentation: Qualify new leads in Google Sheets via OpenAI's GPT-4

## Overview
Automated workflow: Qualify new leads in Google Sheets via OpenAI's GPT-4. This workflow integrates 7 different services: stickyNote, googleSheetsTrigger, merge, set, stopAndError. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `googleSheetsTriggerOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`

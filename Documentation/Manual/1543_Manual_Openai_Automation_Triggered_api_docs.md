# API Documentation: Summarize Google Sheets form feedback via OpenAI's GPT-4

## Overview
Automated workflow: Summarize Google Sheets form feedback via OpenAI's GPT-4. This workflow integrates 8 different services: stickyNote, markdown, stopAndError, manualTrigger, gmail. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

# API Documentation: Resume Screening & Behavioral Interviews with Gemini, Elevenlabs, & Notion ATS copy

## Overview
Automated workflow: Resume Screening & Behavioral Interviews with Gemini, Elevenlabs, & Notion ATS copy. This workflow integrates 20 different services: notionTool, stickyNote, merge, extractFromFile, wait. It contains 77 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 90
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.formTrigger`

### Webhook Endpoints
- **Path**: ``
- **Method**: `POST`
- **Webhook ID**: `a3c17b54-7cd0-496a-af8a-74a6298dcfb4`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.wait`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.notionTool`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `googlePalmApi`
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`

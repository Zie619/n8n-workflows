# API Documentation: Automated Resume Review System Using OpenAI + Google Sheets

## Overview
Automated workflow: Automated Resume Review System Using OpenAI + Google Sheets. This workflow integrates 13 different services: stickyNote, formTrigger, chainLlm, outputParserStructured, merge. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`

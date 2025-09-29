# API Documentation: AI Agent - Cv Resume - Automated Screening , Sorting , Rating and Tracker System

## Overview
Automated workflow: AI Agent - Cv Resume - Automated Screening , Sorting , Rating and Tracker System. This workflow integrates 11 different services: stickyNote, googleDriveTrigger, googleDriveTool, gmailTool, agent. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatGroq`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.googleDocs`
- `n8n-nodes-base.googleSheetsTool`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.googleDriveTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `gmailOAuth2`
- `googleDocsOAuth2Api`
- `googleDriveOAuth2Api`
- `groqApi`

## Environment Variables
- `WEBHOOK_URL`

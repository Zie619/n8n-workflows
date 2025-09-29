# API Documentation: Workflow Results to Markdown Notes in Your Obsidian Vault, via Google Drive

## Overview
Automated workflow: Workflow Results to Markdown Notes in Your Obsidian Vault, via Google Drive. This workflow integrates 9 different services: stickyNote, agent, googleDrive, outputParserStructured, set. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`

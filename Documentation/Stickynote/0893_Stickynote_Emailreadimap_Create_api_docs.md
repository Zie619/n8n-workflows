# API Documentation: Hubspot Workflow

## Overview
Automated workflow: Hubspot Workflow. This workflow integrates 9 different services: stickyNote, hubspot, chainLlm, outputParserStructured, set. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Hubspot
- Hubspot
- Hubspot

## Required Credentials
- `hubspotOAuth2Api`
- `openAiApi`
- `imap`

## Environment Variables
- `BASE_URL`

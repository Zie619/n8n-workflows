# API Documentation: Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls

## Overview
Automated workflow: Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls. This workflow integrates 11 different services: textClassifier, convertToFile, stickyNote, filter, formTrigger. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.extractFromFile`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required

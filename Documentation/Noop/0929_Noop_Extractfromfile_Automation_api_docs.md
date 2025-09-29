# API Documentation: OpenAI e-mail classification - application

## Overview
Automated workflow: OpenAI e-mail classification - application. This workflow integrates 8 different services: textClassifier, stickyNote, informationExtractor, stopAndError, lmChatOpenAi. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.emailReadImap`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `imap`

## Environment Variables
- No environment variables required

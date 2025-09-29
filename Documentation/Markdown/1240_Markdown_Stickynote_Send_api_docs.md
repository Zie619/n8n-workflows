# API Documentation: Very simple Human in the loop system email with AI e IMAP

## Overview
Automated workflow: Very simple Human in the loop system email with AI e IMAP. This workflow integrates 10 different services: stickyNote, markdown, agent, set, stopAndError. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `smtp`
- `imap`

## Environment Variables
- No environment variables required

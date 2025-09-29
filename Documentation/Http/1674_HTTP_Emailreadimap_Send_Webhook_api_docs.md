# API Documentation: Summarize emails with A.I. then send to messenger

## Overview
Automated workflow: Summarize emails with A.I. then send to messenger. This workflow integrates 4 different services: emailReadImap, httpRequest, stopAndError, stickyNote. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`
- `imap`

## Environment Variables
- `API_BASE_URL`

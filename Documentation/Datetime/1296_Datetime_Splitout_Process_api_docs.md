# API Documentation: Parse DMARC reports

## Overview
Automated workflow: Parse DMARC reports. This workflow integrates 14 different services: stickyNote, mySql, compression, splitOut, set. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.renameKeys`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.set`
- `n8n-nodes-base.compression`
- `n8n-nodes-base.mySql`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackOAuth2Api`
- `mySql`
- `imap`

## Environment Variables
- No environment variables required

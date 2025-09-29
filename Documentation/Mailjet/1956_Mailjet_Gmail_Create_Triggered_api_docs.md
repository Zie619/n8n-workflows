# API Documentation: Forward Netflix emails to multiple email addresses with GMail and Mailjet

## Overview
Automated workflow: Forward Netflix emails to multiple email addresses with GMail and Mailjet. This workflow integrates 5 different services: stickyNote, gmailTrigger, splitOut, mailjet, set. It contains 7 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.mailjet`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `mailjetEmailApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required

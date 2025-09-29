# API Documentation: N_01_Simple_Lead_Tracker_Automation_v4

## Overview
Automated workflow: N_01_Simple_Lead_Tracker_Automation_v4. This workflow integrates 9 different services: stickyNote, wait, hubspot, googleSheetsTrigger, stopAndError. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Slack
- Hubspot

## Required Credentials
- `slackOAuth2Api`
- `hubspotOAuth2Api`
- `googleSheetsTriggerOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`

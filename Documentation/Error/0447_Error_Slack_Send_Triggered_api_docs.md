# API Documentation: Slack Workflow

## Overview
Automated workflow: Slack Workflow. This workflow integrates 5 different services: stickyNote, errorTrigger, set, stopAndError, slack. It contains 6 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.errorTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`

## Environment Variables
- No environment variables required

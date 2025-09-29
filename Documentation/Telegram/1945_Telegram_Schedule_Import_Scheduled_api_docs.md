# API Documentation: FetchGithubIssues

## Overview
Automated workflow: FetchGithubIssues. This workflow integrates 7 different services: filter, stickyNote, telegram, scheduleTrigger, set. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Github

## Required Credentials
- `telegramApi`
- `githubApi`

## Environment Variables
- No environment variables required

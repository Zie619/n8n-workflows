# API Documentation: Sync Jira issues with subsequent comments to Notion database

## Overview
Automated workflow: Sync Jira issues with subsequent comments to Notion database. This workflow integrates 6 different services: stickyNote, code, switch, jiraTrigger, if. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.jiraTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.if`
- `n8n-nodes-base.jiraTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`
- `notionApi`

## Environment Variables
- `BASE_URL`

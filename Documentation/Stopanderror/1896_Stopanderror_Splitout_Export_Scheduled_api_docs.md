# API Documentation: Clockify Backup Template

## Overview
Automated workflow: Clockify Backup Template. This workflow integrates 12 different services: filter, httpRequest, stickyNote, scheduleTrigger, splitOut. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.clockify`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Github
- Github
- Github

## Required Credentials
- `githubApi`
- `clockifyApi`

## Environment Variables
- `BASE_URL`

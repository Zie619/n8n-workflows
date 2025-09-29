# API Documentation: Restore your credentials from GitHub

## Overview
Automated workflow: Restore your credentials from GitHub. This workflow integrates 10 different services: stickyNote, httpRequest, splitOut, n8n, set. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.set`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.stopAndError`

## Integrations
- Github

## Required Credentials
- `githubApi`
- `n8nApi`

## Environment Variables
- `BASE_URL`

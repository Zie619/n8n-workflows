# API Documentation: Backup workflows to git repository

## Overview
Automated workflow: Backup workflows to git repository. This workflow integrates 8 different services: stickyNote, code, scheduleTrigger, n8n, set. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`

## Integrations
- Github
- Github
- Github

## Required Credentials
- `githubApi`
- `n8nApi`

## Environment Variables
- No environment variables required

# API Documentation: Workflow Importer

## Overview
Automated workflow: Workflow Importer. This workflow integrates 19 different services: stickyNote, merge, if, removeDuplicates, extractFromFile. It contains 63 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 72
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.form`
- `n8n-nodes-base.code`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.renameKeys`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `n8nApi`

## Environment Variables
- `BASE_URL`

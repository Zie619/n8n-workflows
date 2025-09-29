# API Documentation: Translate

## Overview
Automated workflow: Translate. This workflow integrates 11 different services: convertToFile, stickyNote, formTrigger, googleTranslate, code. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.form`
- `n8n-nodes-base.googleTranslate`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleTranslateOAuth2Api`

## Environment Variables
- No environment variables required

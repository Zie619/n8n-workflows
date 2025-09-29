# API Documentation: Html2Pdf Workflow

## Overview
Automated workflow: Html2Pdf Workflow. This workflow integrates 5 different services: stickyNote, code, PdfToPng, manualTrigger, html2Pdf. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@custom-js/n8n-nodes-pdf-toolkit.PdfToPng`
- `n8n-nodes-base.code`
- `@custom-js/n8n-nodes-pdf-toolkit.html2Pdf`

## Integrations
- No external integrations detected

## Required Credentials
- `customJsApi`

## Environment Variables
- No environment variables required

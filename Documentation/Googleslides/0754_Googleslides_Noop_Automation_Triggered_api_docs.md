# API Documentation: DSP Certificate w/ Google Forms

## Overview
Automated workflow: DSP Certificate w/ Google Forms. This workflow integrates 9 different services: stickyNote, googleSheetsTrigger, googleSlides, googleDrive, set. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSlides`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsTriggerOAuth2Api`
- `gmailOAuth2`
- `googleSlidesOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`

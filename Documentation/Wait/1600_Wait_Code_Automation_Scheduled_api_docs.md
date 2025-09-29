# API Documentation: Phishing_analysis__URLScan_io_and_Virustotal_

## Overview
Automated workflow: Phishing_analysis__URLScan_io_and_Virustotal_. This workflow integrates 14 different services: microsoftOutlook, httpRequest, filter, stickyNote, wait. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.urlScanIo`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Slack
- Microsoft
- Microsoft

## Required Credentials
- `slackApi`
- `virusTotalApi`
- `urlScanIoApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`

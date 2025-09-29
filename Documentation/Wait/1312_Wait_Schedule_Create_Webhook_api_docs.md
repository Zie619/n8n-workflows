# API Documentation: Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a...

## Overview
Automated workflow: Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack. This workflow integrates 10 different services: itemLists, httpRequest, stickyNote, wait, scheduleTrigger. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 48
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.wait`

## Integrations
- Slack

## Required Credentials
- `jiraSoftwareCloudApi`
- `virusTotalApi`
- `slackOAuth2Api`
- `crowdStrikeOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`

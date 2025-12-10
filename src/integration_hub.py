#!/usr/bin/env python3
"""
Integration Hub for N8N Workflows
Connect with external platforms and services.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import httpx
from datetime import datetime


class IntegrationConfig(BaseModel):
    name: str
    api_key: str
    base_url: str
    enabled: bool = True


class WebhookPayload(BaseModel):
    event: str
    data: Dict[str, Any]
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class IntegrationHub:
    def __init__(self):
        self.integrations = {}
        self.webhook_endpoints = {}

    def register_integration(self, config: IntegrationConfig):
        """Register a new integration."""
        self.integrations[config.name] = config

    async def sync_with_github(self, repo: str, token: str) -> Dict[str, Any]:
        """Sync workflows with GitHub repository."""
        try:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": f"token {token}"}

                # Get repository contents
                response = await client.get(
                    f"https://api.github.com/repos/{repo}/contents/workflows",
                    headers=headers,
                )

                if response.status_code == 200:
                    files = response.json()
                    workflow_files = [f for f in files if f["name"].endswith(".json")]

                    return {
                        "status": "success",
                        "repository": repo,
                        "workflow_files": len(workflow_files),
                        "files": [f["name"] for f in workflow_files],
                    }
                else:
                    return {"status": "error", "message": "Failed to access repository"}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def sync_with_slack(self, webhook_url: str, message: str) -> Dict[str, Any]:
        """Send notification to Slack."""
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "text": message,
                    "username": "N8N Workflows Bot",
                    "icon_emoji": ":robot_face:",
                }

                response = await client.post(webhook_url, json=payload)

                if response.status_code == 200:
                    return {
                        "status": "success",
                        "message": "Notification sent to Slack",
                    }
                else:
                    return {"status": "error", "message": "Failed to send to Slack"}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def sync_with_discord(self, webhook_url: str, message: str) -> Dict[str, Any]:
        """Send notification to Discord."""
        try:
            async with httpx.AsyncClient() as client:
                payload = {"content": message, "username": "N8N Workflows Bot"}

                response = await client.post(webhook_url, json=payload)

                if response.status_code == 204:
                    return {
                        "status": "success",
                        "message": "Notification sent to Discord",
                    }
                else:
                    return {"status": "error", "message": "Failed to send to Discord"}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def export_to_airtable(
        self, base_id: str, table_name: str, api_key: str, workflows: List[Dict]
    ) -> Dict[str, Any]:
        """Export workflows to Airtable."""
        try:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": f"Bearer {api_key}"}

                records = []
                for workflow in workflows:
                    record = {
                        "fields": {
                            "Name": workflow.get("name", ""),
                            "Description": workflow.get("description", ""),
                            "Trigger Type": workflow.get("trigger_type", ""),
                            "Complexity": workflow.get("complexity", ""),
                            "Node Count": workflow.get("node_count", 0),
                            "Active": workflow.get("active", False),
                            "Integrations": ", ".join(workflow.get("integrations", [])),
                            "Last Updated": datetime.now().isoformat(),
                        }
                    }
                    records.append(record)

                # Create records in batches
                batch_size = 10
                created_records = 0

                for i in range(0, len(records), batch_size):
                    batch = records[i : i + batch_size]

                    response = await client.post(
                        f"https://api.airtable.com/v0/{base_id}/{table_name}",
                        headers=headers,
                        json={"records": batch},
                    )

                    if response.status_code == 200:
                        created_records += len(batch)
                    else:
                        return {
                            "status": "error",
                            "message": f"Failed to create records: {response.text}",
                        }

                return {
                    "status": "success",
                    "message": f"Exported {created_records} workflows to Airtable",
                }

        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def sync_with_notion(
        self, database_id: str, token: str, workflows: List[Dict]
    ) -> Dict[str, Any]:
        """Sync workflows with Notion database."""
        try:
            async with httpx.AsyncClient() as client:
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Notion-Version": "2022-06-28",
                }

                created_pages = 0

                for workflow in workflows:
                    page_data = {
                        "parent": {"database_id": database_id},
                        "properties": {
                            "Name": {
                                "title": [
                                    {"text": {"content": workflow.get("name", "")}}
                                ]
                            },
                            "Description": {
                                "rich_text": [
                                    {
                                        "text": {
                                            "content": workflow.get("description", "")
                                        }
                                    }
                                ]
                            },
                            "Trigger Type": {
                                "select": {"name": workflow.get("trigger_type", "")}
                            },
                            "Complexity": {
                                "select": {"name": workflow.get("complexity", "")}
                            },
                            "Node Count": {"number": workflow.get("node_count", 0)},
                            "Active": {"checkbox": workflow.get("active", False)},
                            "Integrations": {
                                "multi_select": [
                                    {"name": integration}
                                    for integration in workflow.get("integrations", [])
                                ]
                            },
                        },
                    }

                    response = await client.post(
                        "https://api.notion.com/v1/pages",
                        headers=headers,
                        json=page_data,
                    )

                    if response.status_code == 200:
                        created_pages += 1
                    else:
                        return {
                            "status": "error",
                            "message": f"Failed to create page: {response.text}",
                        }

                return {
                    "status": "success",
                    "message": f"Synced {created_pages} workflows to Notion",
                }

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def register_webhook(self, endpoint: str, handler):
        """Register a webhook endpoint."""
        self.webhook_endpoints[endpoint] = handler

    async def handle_webhook(self, endpoint: str, payload: WebhookPayload):
        """Handle incoming webhook."""
        if endpoint in self.webhook_endpoints:
            return await self.webhook_endpoints[endpoint](payload)
        else:
            return {"status": "error", "message": "Webhook endpoint not found"}


# Initialize integration hub
integration_hub = IntegrationHub()

# FastAPI app for Integration Hub
integration_app = FastAPI(title="N8N Integration Hub", version="1.0.0")


@integration_app.post("/integrations/github/sync")
async def sync_github(repo: str, token: str):
    """Sync workflows with GitHub repository."""
    try:
        result = await integration_hub.sync_with_github(repo, token)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.post("/integrations/slack/notify")
async def notify_slack(webhook_url: str, message: str):
    """Send notification to Slack."""
    try:
        result = await integration_hub.sync_with_slack(webhook_url, message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.post("/integrations/discord/notify")
async def notify_discord(webhook_url: str, message: str):
    """Send notification to Discord."""
    try:
        result = await integration_hub.sync_with_discord(webhook_url, message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.post("/integrations/airtable/export")
async def export_airtable(
    base_id: str, table_name: str, api_key: str, workflows: List[Dict]
):
    """Export workflows to Airtable."""
    try:
        result = await integration_hub.export_to_airtable(
            base_id, table_name, api_key, workflows
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.post("/integrations/notion/sync")
async def sync_notion(database_id: str, token: str, workflows: List[Dict]):
    """Sync workflows with Notion database."""
    try:
        result = await integration_hub.sync_with_notion(database_id, token, workflows)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.post("/webhooks/{endpoint}")
async def handle_webhook_endpoint(endpoint: str, payload: WebhookPayload):
    """Handle incoming webhook."""
    try:
        result = await integration_hub.handle_webhook(endpoint, payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@integration_app.get("/integrations/status")
async def get_integration_status():
    """Get status of all integrations."""
    return {
        "integrations": list(integration_hub.integrations.keys()),
        "webhook_endpoints": list(integration_hub.webhook_endpoints.keys()),
        "status": "operational",
    }


@integration_app.get("/integrations/dashboard")
async def get_integration_dashboard():
    """Get integration dashboard HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N Integration Hub</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            .dashboard {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            .header h1 {
                font-size: 32px;
                margin-bottom: 10px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .integrations-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .integration-card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }
            .integration-card:hover {
                transform: translateY(-5px);
            }
            .integration-icon {
                font-size: 48px;
                margin-bottom: 15px;
            }
            .integration-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #333;
            }
            .integration-description {
                color: #666;
                margin-bottom: 20px;
                line-height: 1.5;
            }
            .integration-actions {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
            }
            .action-btn {
                padding: 10px 20px;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                font-size: 14px;
                transition: all 0.3s ease;
                text-decoration: none;
                display: inline-block;
                text-align: center;
            }
            .btn-primary {
                background: #667eea;
                color: white;
            }
            .btn-primary:hover {
                background: #5a6fd8;
            }
            .btn-secondary {
                background: #f8f9fa;
                color: #666;
                border: 1px solid #e9ecef;
            }
            .btn-secondary:hover {
                background: #e9ecef;
            }
            .status-indicator {
                display: inline-block;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                margin-right: 8px;
            }
            .status-online {
                background: #28a745;
            }
            .status-offline {
                background: #dc3545;
            }
            .webhook-section {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .webhook-endpoint {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                margin: 10px 0;
                font-family: monospace;
                border-left: 4px solid #667eea;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>🔗 N8N Integration Hub</h1>
                <p>Connect your workflows with external platforms and services</p>
            </div>
            
            <div class="integrations-grid">
                <div class="integration-card">
                    <div class="integration-icon">🐙</div>
                    <div class="integration-title">GitHub</div>
                    <div class="integration-description">
                        Sync your workflows with GitHub repositories. 
                        Version control and collaborate on workflow development.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="syncGitHub()">Sync Repository</button>
                        <button class="action-btn btn-secondary" onclick="showGitHubConfig()">Configure</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">💬</div>
                    <div class="integration-title">Slack</div>
                    <div class="integration-description">
                        Send notifications and workflow updates to Slack channels.
                        Keep your team informed about automation activities.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="testSlack()">Test Notification</button>
                        <button class="action-btn btn-secondary" onclick="showSlackConfig()">Configure</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">🎮</div>
                    <div class="integration-title">Discord</div>
                    <div class="integration-description">
                        Integrate with Discord servers for workflow notifications.
                        Perfect for gaming communities and developer teams.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="testDiscord()">Test Notification</button>
                        <button class="action-btn btn-secondary" onclick="showDiscordConfig()">Configure</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">📊</div>
                    <div class="integration-title">Airtable</div>
                    <div class="integration-description">
                        Export workflow data to Airtable for project management.
                        Create databases of your automation workflows.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="exportAirtable()">Export Data</button>
                        <button class="action-btn btn-secondary" onclick="showAirtableConfig()">Configure</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">📝</div>
                    <div class="integration-title">Notion</div>
                    <div class="integration-description">
                        Sync workflows with Notion databases for documentation.
                        Create comprehensive workflow documentation.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="syncNotion()">Sync Database</button>
                        <button class="action-btn btn-secondary" onclick="showNotionConfig()">Configure</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">🔗</div>
                    <div class="integration-title">Webhooks</div>
                    <div class="integration-description">
                        Create custom webhook endpoints for external integrations.
                        Receive data from any service that supports webhooks.
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="createWebhook()">Create Webhook</button>
                        <button class="action-btn btn-secondary" onclick="showWebhookDocs()">Documentation</button>
                    </div>
                </div>
            </div>
            
            <div class="webhook-section">
                <h2>🔗 Webhook Endpoints</h2>
                <p>Available webhook endpoints for external integrations:</p>
                <div class="webhook-endpoint">
                    POST /webhooks/workflow-update<br>
                    <small>Receive notifications when workflows are updated</small>
                </div>
                <div class="webhook-endpoint">
                    POST /webhooks/workflow-execution<br>
                    <small>Receive notifications when workflows are executed</small>
                </div>
                <div class="webhook-endpoint">
                    POST /webhooks/error-report<br>
                    <small>Receive error reports from workflow executions</small>
                </div>
            </div>
        </div>
        
        <script>
            async function syncGitHub() {
                const repo = prompt('Enter GitHub repository (owner/repo):');
                const token = prompt('Enter GitHub token:');
                
                if (repo && token) {
                    try {
                        const response = await fetch('/integrations/github/sync', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({repo, token})
                        });
                        const result = await response.json();
                        alert(result.message || 'GitHub sync completed');
                    } catch (error) {
                        alert('Error syncing with GitHub: ' + error.message);
                    }
                }
            }
            
            async function testSlack() {
                const webhook = prompt('Enter Slack webhook URL:');
                const message = 'Test notification from N8N Integration Hub';
                
                if (webhook) {
                    try {
                        const response = await fetch('/integrations/slack/notify', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({webhook_url: webhook, message})
                        });
                        const result = await response.json();
                        alert(result.message || 'Slack notification sent');
                    } catch (error) {
                        alert('Error sending to Slack: ' + error.message);
                    }
                }
            }
            
            async function testDiscord() {
                const webhook = prompt('Enter Discord webhook URL:');
                const message = 'Test notification from N8N Integration Hub';
                
                if (webhook) {
                    try {
                        const response = await fetch('/integrations/discord/notify', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({webhook_url: webhook, message})
                        });
                        const result = await response.json();
                        alert(result.message || 'Discord notification sent');
                    } catch (error) {
                        alert('Error sending to Discord: ' + error.message);
                    }
                }
            }
            
            function showGitHubConfig() {
                alert('GitHub Configuration:\\n\\n1. Create a GitHub token with repo access\\n2. Use format: owner/repository\\n3. Ensure workflows are in /workflows directory');
            }
            
            function showSlackConfig() {
                alert('Slack Configuration:\\n\\n1. Go to Slack App Directory\\n2. Add "Incoming Webhooks" app\\n3. Create webhook URL\\n4. Use the URL for notifications');
            }
            
            function showDiscordConfig() {
                alert('Discord Configuration:\\n\\n1. Go to Server Settings\\n2. Navigate to Integrations\\n3. Create Webhook\\n4. Copy webhook URL');
            }
            
            function showAirtableConfig() {
                alert('Airtable Configuration:\\n\\n1. Create a new Airtable base\\n2. Get API key from account settings\\n3. Get base ID from API documentation\\n4. Configure table structure');
            }
            
            function showNotionConfig() {
                alert('Notion Configuration:\\n\\n1. Create a Notion integration\\n2. Get integration token\\n3. Create database with proper schema\\n4. Share database with integration');
            }
            
            function createWebhook() {
                alert('Webhook Creation:\\n\\n1. Choose endpoint name\\n2. Configure payload structure\\n3. Set up authentication\\n4. Test webhook endpoint');
            }
            
            function showWebhookDocs() {
                alert('Webhook Documentation:\\n\\nAvailable at: /docs\\n\\nEndpoints:\\n- POST /webhooks/{endpoint}\\n- Payload: {event, data, timestamp}\\n- Response: {status, message}');
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(integration_app, host="127.0.0.1", port=8003)

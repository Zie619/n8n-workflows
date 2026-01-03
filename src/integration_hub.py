#!/usr/bin/env python3
"""
N8N工作流集成中心
与外部平台和服务进行连接。
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import httpx
import json
import asyncio
from datetime import datetime
import os

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
        """注册一个新的集成。"""
        self.integrations[config.name] = config
    
    async def sync_with_github(self, repo: str, token: str) -> Dict[str, Any]:
        """将工作流与GitHub仓库同步。"""
        try:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": f"token {token}"}
                
                # Get repository contents
                response = await client.get(
                    f"https://api.github.com/repos/{repo}/contents/workflows",
                    headers=headers
                )
                
                if response.status_code == 200:
                    files = response.json()
                    workflow_files = [f for f in files if f['name'].endswith('.json')]
                    
                    return {
                        "status": "success",
                        "repository": repo,
                        "workflow_files": len(workflow_files),
                        "files": [f['name'] for f in workflow_files]
                    }
                else:
                    return {"status": "error", "message": "Failed to access repository"}
                    
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def sync_with_slack(self, webhook_url: str, message: str) -> Dict[str, Any]:
        """向Slack发送通知。"""
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "text": message,
                    "username": "N8N Workflows Bot",
                    "icon_emoji": ":robot_face:"
                }
                
                response = await client.post(webhook_url, json=payload)
                
                if response.status_code == 200:
                    return {"status": "success", "message": "Notification sent to Slack"}
                else:
                    return {"status": "error", "message": "Failed to send to Slack"}
                    
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def sync_with_discord(self, webhook_url: str, message: str) -> Dict[str, Any]:
        """向Discord发送通知。"""
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "content": message,
                    "username": "N8N Workflows Bot"
                }
                
                response = await client.post(webhook_url, json=payload)
                
                if response.status_code == 204:
                    return {"status": "success", "message": "Notification sent to Discord"}
                else:
                    return {"status": "error", "message": "Failed to send to Discord"}
                    
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def export_to_airtable(self, base_id: str, table_name: str, api_key: str, workflows: List[Dict]) -> Dict[str, Any]:
        """将工作流导出到Airtable。"""
        try:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": f"Bearer {api_key}"}
                
                records = []
                for workflow in workflows:
                    record = {
                        "fields": {
                            "Name": workflow.get('name', ''),
                            "Description": workflow.get('description', ''),
                            "Trigger Type": workflow.get('trigger_type', ''),
                            "Complexity": workflow.get('complexity', ''),
                            "Node Count": workflow.get('node_count', 0),
                            "Active": workflow.get('active', False),
                            "Integrations": ", ".join(workflow.get('integrations', [])),
                            "Last Updated": datetime.now().isoformat()
                        }
                    }
                    records.append(record)
                
                # Create records in batches
                batch_size = 10
                created_records = 0
                
                for i in range(0, len(records), batch_size):
                    batch = records[i:i + batch_size]
                    
                    response = await client.post(
                        f"https://api.airtable.com/v0/{base_id}/{table_name}",
                        headers=headers,
                        json={"records": batch}
                    )
                    
                    if response.status_code == 200:
                        created_records += len(batch)
                    else:
                        return {"status": "error", "message": f"Failed to create records: {response.text}"}
                
                return {
                    "status": "success",
                    "message": f"Exported {created_records} workflows to Airtable"
                }
                
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def sync_with_notion(self, database_id: str, token: str, workflows: List[Dict]) -> Dict[str, Any]:
        """将工作流与Notion数据库同步。"""
        try:
            async with httpx.AsyncClient() as client:
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Notion-Version": "2022-06-28"
                }
                
                created_pages = 0
                
                for workflow in workflows:
                    page_data = {
                        "parent": {"database_id": database_id},
                        "properties": {
                            "Name": {
                                "title": [{"text": {"content": workflow.get('name', '')}}]
                            },
                            "Description": {
                                "rich_text": [{"text": {"content": workflow.get('description', '')}}]
                            },
                            "Trigger Type": {
                                "select": {"name": workflow.get('trigger_type', '')}
                            },
                            "Complexity": {
                                "select": {"name": workflow.get('complexity', '')}
                            },
                            "Node Count": {
                                "number": workflow.get('node_count', 0)
                            },
                            "Active": {
                                "checkbox": workflow.get('active', False)
                            },
                            "Integrations": {
                                "multi_select": [{"name": integration} for integration in workflow.get('integrations', [])]
                            }
                        }
                    }
                    
                    response = await client.post(
                        "https://api.notion.com/v1/pages",
                        headers=headers,
                        json=page_data
                    )
                    
                    if response.status_code == 200:
                        created_pages += 1
                    else:
                        return {"status": "error", "message": f"Failed to create page: {response.text}"}
                
                return {
                    "status": "success",
                    "message": f"Synced {created_pages} workflows to Notion"
                }
                
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def register_webhook(self, endpoint: str, handler):
        """注册一个webhook端点。"""
        self.webhook_endpoints[endpoint] = handler
    
    async def handle_webhook(self, endpoint: str, payload: WebhookPayload):
        """处理传入的webhook。"""
        if endpoint in self.webhook_endpoints:
            return await self.webhook_endpoints[endpoint](payload)
        else:
            return {"status": "error", "message": "Webhook endpoint not found"}

# Initialize integration hub
integration_hub = IntegrationHub()

# FastAPI应用 - 集成中心
integration_app = FastAPI(title="N8N集成中心", version="1.0.0")

@integration_app.post("/integrations/github/sync")
async def sync_github(repo: str, token: str):
    """将工作流与GitHub仓库同步。"""
    try:
        result = await integration_hub.sync_with_github(repo, token)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.post("/integrations/slack/notify")
async def notify_slack(webhook_url: str, message: str):
    """向Slack发送通知。"""
    try:
        result = await integration_hub.sync_with_slack(webhook_url, message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.post("/integrations/discord/notify")
async def notify_discord(webhook_url: str, message: str):
    """向Discord发送通知。"""
    try:
        result = await integration_hub.sync_with_discord(webhook_url, message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.post("/integrations/airtable/export")
async def export_airtable(
    base_id: str,
    table_name: str,
    api_key: str,
    workflows: List[Dict]
):
    """将工作流导出到Airtable。"""
    try:
        result = await integration_hub.export_to_airtable(base_id, table_name, api_key, workflows)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.post("/integrations/notion/sync")
async def sync_notion(
    database_id: str,
    token: str,
    workflows: List[Dict]
):
    """将工作流与Notion数据库同步。"""
    try:
        result = await integration_hub.sync_with_notion(database_id, token, workflows)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.post("/webhooks/{endpoint}")
async def handle_webhook_endpoint(endpoint: str, payload: WebhookPayload):
    """处理传入的webhook。"""
    try:
        result = await integration_hub.handle_webhook(endpoint, payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@integration_app.get("/integrations/status")
async def get_integration_status():
    """获取所有集成的状态。"""
    return {
        "integrations": list(integration_hub.integrations.keys()),
        "webhook_endpoints": list(integration_hub.webhook_endpoints.keys()),
        "status": "operational"
    }

@integration_app.get("/integrations/dashboard")
async def get_integration_dashboard():
    """获取集成中心仪表板HTML。"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N集成中心</title>
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
                <h1>🔗 N8N集成中心</h1>
                <p>将您的工作流与外部平台和服务连接起来</p>
            </div>
            
            <div class="integrations-grid">
                <div class="integration-card">
                    <div class="integration-icon">🐙</div>
                    <div class="integration-title">GitHub</div>
                    <div class="integration-description">
                        将您的工作流与GitHub仓库同步。
                        版本控制和协作开发工作流。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="syncGitHub()">同步仓库</button>
                        <button class="action-btn btn-secondary" onclick="showGitHubConfig()">配置</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">💬</div>
                    <div class="integration-title">Slack</div>
                    <div class="integration-description">
                        向Slack频道发送通知和工作流更新。
                        让您的团队了解自动化活动。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="testSlack()">测试通知</button>
                        <button class="action-btn btn-secondary" onclick="showSlackConfig()">配置</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">🎮</div>
                    <div class="integration-title">Discord</div>
                    <div class="integration-description">
                        与Discord服务器集成以获取工作流通知。
                        适用于游戏社区和开发团队。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="testDiscord()">测试通知</button>
                        <button class="action-btn btn-secondary" onclick="showDiscordConfig()">配置</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">📊</div>
                    <div class="integration-title">Airtable</div>
                    <div class="integration-description">
                        将工作流数据导出到Airtable进行项目管理。
                        创建您的自动化工作流数据库。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="exportAirtable()">导出数据</button>
                        <button class="action-btn btn-secondary" onclick="showAirtableConfig()">配置</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">📝</div>
                    <div class="integration-title">Notion</div>
                    <div class="integration-description">
                        将工作流与Notion数据库同步以进行文档记录。
                        创建全面的工作流文档。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="syncNotion()">同步数据库</button>
                        <button class="action-btn btn-secondary" onclick="showNotionConfig()">配置</button>
                    </div>
                </div>
                
                <div class="integration-card">
                    <div class="integration-icon">🔗</div>
                    <div class="integration-title">Webhooks</div>
                    <div class="integration-description">
                        为外部集成创建自定义webhook端点。
                        接收来自任何支持webhooks的服务的数据。
                    </div>
                    <div class="integration-actions">
                        <button class="action-btn btn-primary" onclick="createWebhook()">创建Webhook</button>
                        <button class="action-btn btn-secondary" onclick="showWebhookDocs()">文档</button>
                    </div>
                </div>
            </div>
            
            <div class="webhook-section">
                <h2>🔗 Webhook端点</h2>
                <p>可供外部集成使用的webhook端点：</p>
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
                const repo = prompt('请输入GitHub仓库 (owner/repo)：');
                const token = prompt('请输入GitHub令牌：');
                
                if (repo && token) {
                    try {
                        const response = await fetch('/integrations/github/sync', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({repo, token})
                        });
                        const result = await response.json();
                        alert(result.message || 'GitHub同步完成');
                    } catch (error) {
                        alert('GitHub同步错误：' + error.message);
                    }
                }
            }
            
            async function testSlack() {
                const webhook = prompt('请输入Slack webhook URL：');
                const message = '来自N8N集成中心的测试通知';
                
                if (webhook) {
                    try {
                        const response = await fetch('/integrations/slack/notify', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({webhook_url: webhook, message})
                        });
                        const result = await response.json();
                        alert(result.message || 'Slack通知已发送');
                    } catch (error) {
                        alert('发送到Slack错误：' + error.message);
                    }
                }
            }
            
            async function testDiscord() {
                const webhook = prompt('请输入Discord webhook URL：');
                const message = '来自N8N集成中心的测试通知';
                
                if (webhook) {
                    try {
                        const response = await fetch('/integrations/discord/notify', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({webhook_url: webhook, message})
                        });
                        const result = await response.json();
                        alert(result.message || 'Discord通知已发送');
                    } catch (error) {
                        alert('发送到Discord错误：' + error.message);
                    }
                }
            }
            
            function showGitHubConfig() {
                alert('GitHub配置：\n\n1. 创建一个具有repo访问权限的GitHub令牌\n2. 使用格式：owner/repository\n3. 确保工作流位于/workflows目录中');
            }
            
            function showSlackConfig() {
                alert('Slack配置：\n\n1. 转到Slack应用目录\n2. 添加"Incoming Webhooks"应用\n3. 创建webhook URL\n4. 使用该URL发送通知');
            }
            
            function showDiscordConfig() {
                alert('Discord配置：\n\n1. 转到服务器设置\n2. 导航到集成\n3. 创建Webhook\n4. 复制webhook URL');
            }
            
            function showAirtableConfig() {
                alert('Airtable配置：\n\n1. 创建一个新的Airtable工作区\n2. 从账户设置获取API密钥\n3. 从API文档获取工作区ID\n4. 配置表格结构');
            }
            
            function showNotionConfig() {
                alert('Notion配置：\n\n1. 创建一个Notion集成\n2. 获取集成令牌\n3. 创建具有适当架构的数据库\n4. 与集成共享数据库');
            }
            
            function createWebhook() {
                alert('Webhook创建：\n\n1. 选择端点名称\n2. 配置负载结构\n3. 设置认证\n4. 测试webhook端点');
            }
            
            function showWebhookDocs() {
                alert('Webhook文档：\n\n可访问：/docs\n\n端点：\n- POST /webhooks/{endpoint}\n- 负载：{event, data, timestamp}\n- 响应：{status, message}');
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(integration_app, host="127.0.0.1", port=8003)

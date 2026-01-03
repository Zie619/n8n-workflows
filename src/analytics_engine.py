#!/usr/bin/env python3
"""
N8N 工作流高级分析引擎
提供洞察、模式和使用分析。
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import sqlite3
import json
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import statistics

class AnalyticsResponse(BaseModel):
    overview: Dict[str, Any]
    trends: Dict[str, Any]
    patterns: Dict[str, Any]
    recommendations: List[str]
    generated_at: str

class WorkflowAnalytics:
    def __init__(self, db_path: str = "workflows.db"):
        self.db_path = db_path
    
    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def get_workflow_analytics(self) -> Dict[str, Any]:
        """获取全面的工作流分析。"""
        conn = self.get_db_connection()
        
        # 基本统计
        cursor = conn.execute("SELECT COUNT(*) as total FROM workflows")
        total_workflows = cursor.fetchone()['total']
        
        cursor = conn.execute("SELECT COUNT(*) as active FROM workflows WHERE active = 1")
        active_workflows = cursor.fetchone()['active']
        
        # 触发器类型分布
        cursor = conn.execute("""
            SELECT trigger_type, COUNT(*) as count 
            FROM workflows 
            GROUP BY trigger_type 
            ORDER BY count DESC
        """)
        trigger_distribution = {row['trigger_type']: row['count'] for row in cursor.fetchall()}
        
        # 复杂度分布
        cursor = conn.execute("""
            SELECT complexity, COUNT(*) as count 
            FROM workflows 
            GROUP BY complexity 
            ORDER BY count DESC
        """)
        complexity_distribution = {row['complexity']: row['count'] for row in cursor.fetchall()}
        
        # 节点数量统计
        cursor = conn.execute("""
            SELECT 
                AVG(node_count) as avg_nodes,
                MIN(node_count) as min_nodes,
                MAX(node_count) as max_nodes,
                COUNT(*) as total
            FROM workflows
        """)
        node_stats = dict(cursor.fetchone())
        
        # 集成分析
        cursor = conn.execute("SELECT integrations FROM workflows WHERE integrations IS NOT NULL")
        all_integrations = []
        for row in cursor.fetchall():
            integrations = json.loads(row['integrations'] or '[]')
            all_integrations.extend(integrations)
        
        integration_counts = Counter(all_integrations)
        top_integrations = dict(integration_counts.most_common(10))
        
        # 工作流模式
        patterns = self.analyze_workflow_patterns(conn)
        
        # 建议
        recommendations = self.generate_recommendations(
            total_workflows, active_workflows, trigger_distribution, 
            complexity_distribution, top_integrations
        )
        
        conn.close()
        
        return {
            "overview": {
                "total_workflows": total_workflows,
                "active_workflows": active_workflows,
                "activation_rate": round((active_workflows / total_workflows) * 100, 2) if total_workflows > 0 else 0,
                "unique_integrations": len(integration_counts),
                "avg_nodes_per_workflow": round(node_stats['avg_nodes'], 2),
                "most_complex_workflow": node_stats['max_nodes']
            },
            "distributions": {
                "trigger_types": trigger_distribution,
                "complexity_levels": complexity_distribution,
                "top_integrations": top_integrations
            },
            "patterns": patterns,
            "recommendations": recommendations,
            "generated_at": datetime.now().isoformat()
        }
    
    def analyze_workflow_patterns(self, conn) -> Dict[str, Any]:
        """分析常见的工作流模式和关系。"""
        # 集成共现分析
        cursor = conn.execute("""
            SELECT name, integrations, trigger_type, complexity, node_count
            FROM workflows 
            WHERE integrations IS NOT NULL
        """)
        
        integration_pairs = defaultdict(int)
        service_categories = defaultdict(int)
        
        for row in cursor.fetchall():
            integrations = json.loads(row['integrations'] or '[]')
            
            # 统计服务类别
            for integration in integrations:
                category = self.categorize_service(integration)
                service_categories[category] += 1
            
            # 查找集成对
            for i in range(len(integrations)):
                for j in range(i + 1, len(integrations)):
                    pair = tuple(sorted([integrations[i], integrations[j]]))
                integration_pairs[pair] += 1
        
        # 最常见的集成对
        top_pairs = dict(Counter(integration_pairs).most_common(5))
        
        # 工作流复杂度模式
        cursor = conn.execute("""
            SELECT 
                trigger_type,
                complexity,
                AVG(node_count) as avg_nodes,
                COUNT(*) as count
            FROM workflows 
            GROUP BY trigger_type, complexity
            ORDER BY count DESC
        """)
        
        complexity_patterns = []
        for row in cursor.fetchall():
            complexity_patterns.append({
                "trigger_type": row['trigger_type'],
                "complexity": row['complexity'],
                "avg_nodes": round(row['avg_nodes'], 2),
                "frequency": row['count']
            })
        
        return {
            "integration_pairs": top_pairs,
            "service_categories": dict(service_categories),
            "complexity_patterns": complexity_patterns[:10]
        }
    
    def categorize_service(self, service: str) -> str:
        """将服务分类到更广泛的类别中。"""
        service_lower = service.lower()
        
        if any(word in service_lower for word in ['slack', 'telegram', 'discord', 'whatsapp']):
            return "通信"
        elif any(word in service_lower for word in ['openai', 'ai', 'chat', 'gpt']):
            return "人工智能/机器学习"
        elif any(word in service_lower for word in ['google', 'microsoft', 'office']):
            return "生产力"
        elif any(word in service_lower for word in ['shopify', 'woocommerce', 'stripe']):
            return "电子商务"
        elif any(word in service_lower for word in ['airtable', 'notion', 'database']):
            return "数据管理"
        elif any(word in service_lower for word in ['twitter', 'facebook', 'instagram']):
            return "社交媒体"
        else:
            return "其他"
    
    def generate_recommendations(self, total: int, active: int, triggers: Dict, 
                               complexity: Dict, integrations: Dict) -> List[str]:
        """基于分析生成可操作的建议。"""
        recommendations = []
        
        # 激活率建议
        activation_rate = (active / total) * 100 if total > 0 else 0
        if activation_rate < 20:
            recommendations.append(
                f"激活率较低 ({activation_rate:.1f}%)。考虑审查非活跃工作流 "
                "并更新它们以适应当前用例。"
            )
        elif activation_rate > 80:
            recommendations.append(
                f"激活率较高 ({activation_rate:.1f}%)！您的工作流维护良好。 "
                "考虑记录成功的模式以便团队共享。"
            )
        
        # 触发器类型建议
        webhook_count = triggers.get('Webhook', 0)
        scheduled_count = triggers.get('Scheduled', 0)
        
        if webhook_count > scheduled_count * 2:
            recommendations.append(
                "您有许多 Webhook 触发的工作流。考虑添加计划工作流 "
                "用于数据同步和维护任务。"
            )
        elif scheduled_count > webhook_count * 2:
            recommendations.append(
                "您有许多计划工作流。考虑添加 Webhook 触发的工作流 "
                "用于实时集成和事件驱动的自动化。"
            )
        
        # 集成建议
        if 'OpenAI' in integrations and integrations['OpenAI'] > 5:
            recommendations.append(
                "您广泛使用 OpenAI。考虑创建 AI 工作流模板 "
                "用于常见用例，如内容生成和数据分析。"
            )
        
        if 'Slack' in integrations and 'Telegram' in integrations:
            recommendations.append(
                "您使用多个通信平台。考虑创建统一 "
                "通知工作流，可以发送到多个渠道。"
            )
        
        # 复杂度建议
        high_complexity = complexity.get('high', 0)
        if high_complexity > total * 0.3:
            recommendations.append(
                "您有许多高复杂度的工作流。考虑将它们分解为 "
                "更小的、可重用的组件以提高可维护性。"
            )
        
        return recommendations
    
    def get_trend_analysis(self, days: int = 30) -> Dict[str, Any]:
        """分析随时间变化的趋势（演示模拟）。"""
        # 在实际实现中，这将分析历史数据
        return {
            "workflow_growth": {
                "daily_average": 2.3,
                "growth_rate": 15.2,
                "trend": "增长中"
            },
            "popular_integrations": {
                "trending_up": ["OpenAI", "Slack", "Google Sheets"],
                "trending_down": ["Twitter", "Facebook"],
                "stable": ["Telegram", "Airtable"]
            },
            "complexity_trends": {
                "average_nodes": 12.5,
                "complexity_increase": 8.3,
                "automation_maturity": "中级"
            }
        }
    
    def get_usage_insights(self) -> Dict[str, Any]:
        """获取使用洞察和模式。"""
        conn = self.get_db_connection()
        
        # 活跃与非活跃分析
        cursor = conn.execute("""
            SELECT 
                trigger_type,
                complexity,
                COUNT(*) as total,
                SUM(active) as active_count
            FROM workflows 
            GROUP BY trigger_type, complexity
        """)
        
        usage_patterns = []
        for row in cursor.fetchall():
            activation_rate = (row['active_count'] / row['total']) * 100 if row['total'] > 0 else 0
            usage_patterns.append({
                "trigger_type": row['trigger_type'],
                "complexity": row['complexity'],
                "total_workflows": row['total'],
                "active_workflows": row['active_count'],
                "activation_rate": round(activation_rate, 2)
            })
        
        # 最有效的模式
        effective_patterns = sorted(usage_patterns, key=lambda x: x['activation_rate'], reverse=True)[:5]
        
        conn.close()
        
        return {
            "usage_patterns": usage_patterns,
            "most_effective_patterns": effective_patterns,
            "insights": [
                "Webhook 触发的工作流具有更高的激活率",
                "中等复杂度的工作流最常用",
                "AI 驱动的工作流显示出增加的采用率",
                "通信集成最受欢迎"
            ]
        }

# 初始化分析引擎
analytics_engine = WorkflowAnalytics()

# 用于分析的 FastAPI 应用
analytics_app = FastAPI(title="N8N 分析引擎", version="1.0.0")

@analytics_app.get("/analytics/overview", response_model=AnalyticsResponse)
async def get_analytics_overview():
    """获取全面的分析概览。"""
    try:
        analytics_data = analytics_engine.get_workflow_analytics()
        trends = analytics_engine.get_trend_analysis()
        insights = analytics_engine.get_usage_insights()
        
        return AnalyticsResponse(
            overview=analytics_data["overview"],
            trends=trends,
            patterns=analytics_data["patterns"],
            recommendations=analytics_data["recommendations"],
            generated_at=analytics_data["generated_at"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"分析错误：{str(e)}")

@analytics_app.get("/analytics/trends")
async def get_trend_analysis(days: int = Query(30, ge=1, le=365)):
    """获取指定期间的趋势分析。"""
    try:
        return analytics_engine.get_trend_analysis(days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"趋势分析错误：{str(e)}")

@analytics_app.get("/analytics/insights")
async def get_usage_insights():
    """获取使用洞察和模式。"""
    try:
        return analytics_engine.get_usage_insights()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"洞察错误：{str(e)}")

@analytics_app.get("/analytics/dashboard")
async def get_analytics_dashboard():
    """获取分析仪表板 HTML。"""
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N 分析仪表板</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f8f9fa;
                color: #333;
            }
            .dashboard {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
            }
            .header h1 {
                font-size: 32px;
                margin-bottom: 10px;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .stat-card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            .stat-number {
                font-size: 36px;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 10px;
            }
            .stat-label {
                color: #666;
                font-size: 16px;
            }
            .chart-container {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .chart-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #333;
            }
            .recommendations {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .recommendation {
                background: #e3f2fd;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
                border-left: 4px solid #2196f3;
            }
            .loading {
                text-align: center;
                padding: 40px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>📊 N8N 分析仪表板</h1>
                <p>全面洞察您的工作流生态系统</p>
            </div>
            
            <div class="stats-grid" id="statsGrid">
                <div class="loading">正在加载分析...</div>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">工作流分布</div>
                <canvas id="triggerChart" width="400" height="200"></canvas>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">集成使用情况</div>
                <canvas id="integrationChart" width="400" height="200"></canvas>
            </div>
            
            <div class="recommendations" id="recommendations">
                <div class="chart-title">建议</div>
                <div class="loading">正在加载建议...</div>
            </div>
        </div>
        
        <script>
            async function loadAnalytics() {
                try {
                    const response = await fetch('/analytics/overview');
                    const data = await response.json();
                    
                    // 更新统计
                    updateStats(data.overview);
                    
                    // 创建图表
                    createTriggerChart(data.patterns.distributions?.trigger_types || {});
                    createIntegrationChart(data.patterns.distributions?.top_integrations || {});
                    
                    // 更新建议
                    updateRecommendations(data.recommendations);
                    
                } catch (error) {
                    console.error('加载分析时出错:', error);
                    document.getElementById('statsGrid').innerHTML = 
                        '<div class="loading">加载分析时出错。请重试。</div>';
                }
            }
            
            function updateStats(overview) {
                const statsGrid = document.getElementById('statsGrid');
                statsGrid.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-number">${overview.total_workflows?.toLocaleString() || 0}</div>
                        <div class="stat-label">工作流总数</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.active_workflows?.toLocaleString() || 0}</div>
                        <div class="stat-label">活跃工作流</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.activation_rate || 0}%</div>
                        <div class="stat-label">激活率</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.unique_integrations || 0}</div>
                        <div class="stat-label">唯一集成</div>
                    </div>
                `;
            }
            
            function createTriggerChart(triggerData) {
                const ctx = document.getElementById('triggerChart').getContext('2d');
                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: Object.keys(triggerData),
                        datasets: [{
                            data: Object.values(triggerData),
                            backgroundColor: [
                                '#667eea',
                                '#764ba2',
                                '#f093fb',
                                '#f5576c',
                                '#4facfe'
                            ]
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }
                });
            }
            
            function createIntegrationChart(integrationData) {
                const ctx = document.getElementById('integrationChart').getContext('2d');
                const labels = Object.keys(integrationData).slice(0, 10);
                const data = Object.values(integrationData).slice(0, 10);
                
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: '使用次数',
                            data: data,
                            backgroundColor: '#667eea'
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
            
            function updateRecommendations(recommendations) {
                const container = document.getElementById('recommendations');
                if (recommendations && recommendations.length > 0) {
                    container.innerHTML = `
                        <div class="chart-title">建议</div>
                        ${recommendations.map(rec => `
                            <div class="recommendation">${rec}</div>
                        `).join('')}
                    `;
                } else {
                    container.innerHTML = '<div class="chart-title">建议</div><div class="loading">暂无可用建议</div>';
                }
            }
            
            // 页面加载时加载分析
            loadAnalytics();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(analytics_app, host="127.0.0.1", port=8002)

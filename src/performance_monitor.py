#!/usr/bin/env python3
"""
Performance Monitoring System for N8N Workflows
Real-time metrics, monitoring, and alerting.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio
import time
import psutil
from datetime import datetime, timedelta
import json
import threading
import queue
import os


class PerformanceMetrics(BaseModel):
    timestamp: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_io: Dict[str, int]
    api_response_times: Dict[str, float]
    active_connections: int
    database_size: int
    workflow_executions: int
    error_rate: float


class Alert(BaseModel):
    id: str
    type: str
    severity: str
    message: str
    timestamp: str
    resolved: bool = False


class PerformanceMonitor:
    def __init__(self, db_path: str = "workflows.db"):
        self.db_path = db_path
        self.metrics_history = []
        self.alerts = []
        self.websocket_connections = []
        self.monitoring_active = False
        self.metrics_queue = queue.Queue()

    def start_monitoring(self):
        """Start performance monitoring in background thread."""
        if not self.monitoring_active:
            self.monitoring_active = True
            monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            monitor_thread.start()

    def _monitor_loop(self):
        """Main monitoring loop."""
        while self.monitoring_active:
            try:
                metrics = self._collect_metrics()
                self.metrics_history.append(metrics)

                # Keep only last 1000 metrics
                if len(self.metrics_history) > 1000:
                    self.metrics_history = self.metrics_history[-1000:]

                # Check for alerts
                self._check_alerts(metrics)

                # Send to websocket connections
                self._broadcast_metrics(metrics)

                time.sleep(5)  # Collect metrics every 5 seconds

            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(10)

    def _collect_metrics(self) -> PerformanceMetrics:
        """Collect current system metrics."""
        # CPU and Memory
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        # Disk usage
        disk = psutil.disk_usage("/")
        disk_usage = (disk.used / disk.total) * 100

        # Network I/O
        network = psutil.net_io_counters()
        network_io = {
            "bytes_sent": network.bytes_sent,
            "bytes_recv": network.bytes_recv,
            "packets_sent": network.packets_sent,
            "packets_recv": network.packets_recv,
        }

        # API response times (simulated)
        api_response_times = {
            "/api/stats": self._measure_api_time("/api/stats"),
            "/api/workflows": self._measure_api_time("/api/workflows"),
            "/api/search": self._measure_api_time("/api/workflows?q=test"),
        }

        # Active connections
        active_connections = len(psutil.net_connections())

        # Database size
        try:
            db_size = (
                os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0
            )
        except:
            db_size = 0

        # Workflow executions (simulated)
        workflow_executions = self._get_workflow_executions()

        # Error rate (simulated)
        error_rate = self._calculate_error_rate()

        return PerformanceMetrics(
            timestamp=datetime.now().isoformat(),
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            disk_usage=disk_usage,
            network_io=network_io,
            api_response_times=api_response_times,
            active_connections=active_connections,
            database_size=db_size,
            workflow_executions=workflow_executions,
            error_rate=error_rate,
        )

    def _measure_api_time(self, endpoint: str) -> float:
        """Measure API response time (simulated)."""
        # In a real implementation, this would make actual HTTP requests
        import random

        return round(random.uniform(10, 100), 2)

    def _get_workflow_executions(self) -> int:
        """Get number of workflow executions (simulated)."""
        # In a real implementation, this would query execution logs
        import random

        return random.randint(0, 50)

    def _calculate_error_rate(self) -> float:
        """Calculate error rate (simulated)."""
        # In a real implementation, this would analyze error logs
        import random

        return round(random.uniform(0, 5), 2)

    def _check_alerts(self, metrics: PerformanceMetrics):
        """Check metrics against alert thresholds."""
        # CPU alert
        if metrics.cpu_usage > 80:
            self._create_alert(
                "high_cpu", "warning", f"High CPU usage: {metrics.cpu_usage}%"
            )

        # Memory alert
        if metrics.memory_usage > 85:
            self._create_alert(
                "high_memory", "warning", f"High memory usage: {metrics.memory_usage}%"
            )

        # Disk alert
        if metrics.disk_usage > 90:
            self._create_alert(
                "high_disk", "critical", f"High disk usage: {metrics.disk_usage}%"
            )

        # API response time alert
        for endpoint, response_time in metrics.api_response_times.items():
            if response_time > 1000:  # 1 second
                self._create_alert(
                    "slow_api",
                    "warning",
                    f"Slow API response: {endpoint} ({response_time}ms)",
                )

        # Error rate alert
        if metrics.error_rate > 10:
            self._create_alert(
                "high_error_rate", "critical", f"High error rate: {metrics.error_rate}%"
            )

    def _create_alert(self, alert_type: str, severity: str, message: str):
        """Create a new alert."""
        alert = Alert(
            id=f"{alert_type}_{int(time.time())}",
            type=alert_type,
            severity=severity,
            message=message,
            timestamp=datetime.now().isoformat(),
        )

        # Check if similar alert already exists
        existing_alert = next(
            (a for a in self.alerts if a.type == alert_type and not a.resolved), None
        )
        if not existing_alert:
            self.alerts.append(alert)
            self._broadcast_alert(alert)

    def _broadcast_metrics(self, metrics: PerformanceMetrics):
        """Broadcast metrics to all websocket connections."""
        if self.websocket_connections:
            message = {"type": "metrics", "data": metrics.dict()}
            self._broadcast_to_websockets(message)

    def _broadcast_alert(self, alert: Alert):
        """Broadcast alert to all websocket connections."""
        message = {"type": "alert", "data": alert.dict()}
        self._broadcast_to_websockets(message)

    def _broadcast_to_websockets(self, message: dict):
        """Broadcast message to all websocket connections."""
        disconnected = []
        for websocket in self.websocket_connections:
            try:
                asyncio.create_task(websocket.send_text(json.dumps(message)))
            except:
                disconnected.append(websocket)

        # Remove disconnected connections
        for ws in disconnected:
            self.websocket_connections.remove(ws)

    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get performance metrics summary."""
        if not self.metrics_history:
            return {"message": "No metrics available"}

        latest = self.metrics_history[-1]
        avg_cpu = sum(m.cpu_usage for m in self.metrics_history[-10:]) / min(
            10, len(self.metrics_history)
        )
        avg_memory = sum(m.memory_usage for m in self.metrics_history[-10:]) / min(
            10, len(self.metrics_history)
        )

        return {
            "current": latest.dict(),
            "averages": {
                "cpu_usage": round(avg_cpu, 2),
                "memory_usage": round(avg_memory, 2),
            },
            "alerts": [alert.dict() for alert in self.alerts[-10:]],
            "status": "healthy"
            if latest.cpu_usage < 80 and latest.memory_usage < 85
            else "warning",
        }

    def get_historical_metrics(self, hours: int = 24) -> List[Dict]:
        """Get historical metrics for specified hours."""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        cutoff_timestamp = cutoff_time.isoformat()

        return [
            metrics.dict()
            for metrics in self.metrics_history
            if metrics.timestamp >= cutoff_timestamp
        ]

    def resolve_alert(self, alert_id: str) -> bool:
        """Resolve an alert."""
        for alert in self.alerts:
            if alert.id == alert_id:
                alert.resolved = True
                return True
        return False


# Initialize performance monitor
performance_monitor = PerformanceMonitor()
performance_monitor.start_monitoring()

# FastAPI app for Performance Monitoring
monitor_app = FastAPI(title="N8N Performance Monitor", version="1.0.0")


@monitor_app.get("/monitor/metrics")
async def get_current_metrics():
    """Get current performance metrics."""
    return performance_monitor.get_metrics_summary()


@monitor_app.get("/monitor/history")
async def get_historical_metrics(hours: int = 24):
    """Get historical performance metrics."""
    return performance_monitor.get_historical_metrics(hours)


@monitor_app.get("/monitor/alerts")
async def get_alerts():
    """Get current alerts."""
    return [alert.dict() for alert in performance_monitor.alerts if not alert.resolved]


@monitor_app.post("/monitor/alerts/{alert_id}/resolve")
async def resolve_alert(alert_id: str):
    """Resolve an alert."""
    success = performance_monitor.resolve_alert(alert_id)
    if success:
        return {"message": "Alert resolved"}
    else:
        return {"message": "Alert not found"}


@monitor_app.websocket("/monitor/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time metrics."""
    await websocket.accept()
    performance_monitor.websocket_connections.append(websocket)

    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        performance_monitor.websocket_connections.remove(websocket)


@monitor_app.get("/monitor/dashboard")
async def get_monitoring_dashboard():
    """Get performance monitoring dashboard HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N Performance Monitor</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f8f9fa;
                color: #333;
            }
            .dashboard {
                max-width: 1400px;
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
            .metrics-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .metric-card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                text-align: center;
            }
            .metric-value {
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .metric-value.cpu { color: #667eea; }
            .metric-value.memory { color: #28a745; }
            .metric-value.disk { color: #ffc107; }
            .metric-value.network { color: #17a2b8; }
            .metric-label {
                color: #666;
                font-size: 16px;
            }
            .status-indicator {
                display: inline-block;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                margin-right: 8px;
            }
            .status-healthy { background: #28a745; }
            .status-warning { background: #ffc107; }
            .status-critical { background: #dc3545; }
            .chart-container {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .chart-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #333;
            }
            .alerts-section {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            .alert {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
                border-left: 4px solid #667eea;
            }
            .alert.warning {
                border-left-color: #ffc107;
                background: #fff3cd;
            }
            .alert.critical {
                border-left-color: #dc3545;
                background: #f8d7da;
            }
            .alert-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 5px;
            }
            .alert-type {
                font-weight: bold;
                color: #333;
            }
            .alert-severity {
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: bold;
                text-transform: uppercase;
            }
            .severity-warning {
                background: #ffc107;
                color: #856404;
            }
            .severity-critical {
                background: #dc3545;
                color: white;
            }
            .alert-message {
                color: #666;
                font-size: 14px;
            }
            .alert-timestamp {
                color: #999;
                font-size: 12px;
                margin-top: 5px;
            }
            .resolve-btn {
                background: #28a745;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 12px;
            }
            .resolve-btn:hover {
                background: #218838;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>📊 N8N Performance Monitor</h1>
                <p>Real-time system monitoring and alerting</p>
                <div id="connectionStatus">
                    <span class="status-indicator" id="statusIndicator"></span>
                    <span id="statusText">Connecting...</span>
                </div>
            </div>
            
            <div class="metrics-grid" id="metricsGrid">
                <div class="loading">Loading metrics...</div>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">CPU & Memory Usage</div>
                <canvas id="performanceChart" width="400" height="200"></canvas>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">API Response Times</div>
                <canvas id="apiChart" width="400" height="200"></canvas>
            </div>
            
            <div class="alerts-section">
                <div class="chart-title">Active Alerts</div>
                <div id="alertsContainer">
                    <div class="loading">Loading alerts...</div>
                </div>
            </div>
        </div>
        
        <script>
            let ws = null;
            let performanceChart = null;
            let apiChart = null;
            let metricsData = [];
            
            function connectWebSocket() {
                const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
                const wsUrl = `${protocol}//${window.location.host}/monitor/ws`;
                
                ws = new WebSocket(wsUrl);
                
                ws.onopen = function() {
                    updateConnectionStatus(true);
                    loadInitialData();
                };
                
                ws.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    
                    if (data.type === 'metrics') {
                        updateMetrics(data.data);
                        updateCharts(data.data);
                    } else if (data.type === 'alert') {
                        addAlert(data.data);
                    }
                };
                
                ws.onclose = function() {
                    updateConnectionStatus(false);
                    setTimeout(connectWebSocket, 5000);
                };
                
                ws.onerror = function() {
                    updateConnectionStatus(false);
                };
            }
            
            function updateConnectionStatus(connected) {
                const indicator = document.getElementById('statusIndicator');
                const text = document.getElementById('statusText');
                
                if (connected) {
                    indicator.className = 'status-indicator status-healthy';
                    text.textContent = 'Connected';
                } else {
                    indicator.className = 'status-indicator status-critical';
                    text.textContent = 'Disconnected';
                }
            }
            
            async function loadInitialData() {
                try {
                    // Load current metrics
                    const metricsResponse = await fetch('/monitor/metrics');
                    const metrics = await metricsResponse.json();
                    updateMetrics(metrics.current);
                    
                    // Load alerts
                    const alertsResponse = await fetch('/monitor/alerts');
                    const alerts = await alertsResponse.json();
                    displayAlerts(alerts);
                    
                } catch (error) {
                    console.error('Error loading initial data:', error);
                }
            }
            
            function updateMetrics(metrics) {
                const grid = document.getElementById('metricsGrid');
                grid.innerHTML = `
                    <div class="metric-card">
                        <div class="metric-value cpu">${metrics.cpu_usage?.toFixed(1) || 0}%</div>
                        <div class="metric-label">CPU Usage</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value memory">${metrics.memory_usage?.toFixed(1) || 0}%</div>
                        <div class="metric-label">Memory Usage</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value disk">${metrics.disk_usage?.toFixed(1) || 0}%</div>
                        <div class="metric-label">Disk Usage</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value network">${metrics.active_connections || 0}</div>
                        <div class="metric-label">Active Connections</div>
                    </div>
                `;
                
                metricsData.push(metrics);
                if (metricsData.length > 20) {
                    metricsData = metricsData.slice(-20);
                }
            }
            
            function updateCharts(metrics) {
                if (!performanceChart) {
                    initPerformanceChart();
                }
                if (!apiChart) {
                    initApiChart();
                }
                
                // Update performance chart
                const labels = metricsData.map((_, i) => i);
                performanceChart.data.labels = labels;
                performanceChart.data.datasets[0].data = metricsData.map(m => m.cpu_usage);
                performanceChart.data.datasets[1].data = metricsData.map(m => m.memory_usage);
                performanceChart.update();
                
                // Update API chart
                if (metrics.api_response_times) {
                    const endpoints = Object.keys(metrics.api_response_times);
                    const times = Object.values(metrics.api_response_times);
                    apiChart.data.labels = endpoints;
                    apiChart.data.datasets[0].data = times;
                    apiChart.update();
                }
            }
            
            function initPerformanceChart() {
                const ctx = document.getElementById('performanceChart').getContext('2d');
                performanceChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: [],
                        datasets: [{
                            label: 'CPU Usage (%)',
                            data: [],
                            borderColor: '#667eea',
                            backgroundColor: 'rgba(102, 126, 234, 0.1)',
                            tension: 0.4
                        }, {
                            label: 'Memory Usage (%)',
                            data: [],
                            borderColor: '#28a745',
                            backgroundColor: 'rgba(40, 167, 69, 0.1)',
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100
                            }
                        }
                    }
                });
            }
            
            function initApiChart() {
                const ctx = document.getElementById('apiChart').getContext('2d');
                apiChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: [],
                        datasets: [{
                            label: 'Response Time (ms)',
                            data: [],
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
            
            function displayAlerts(alerts) {
                const container = document.getElementById('alertsContainer');
                
                if (alerts.length === 0) {
                    container.innerHTML = '<div class="loading">No active alerts</div>';
                    return;
                }
                
                container.innerHTML = alerts.map(alert => `
                    <div class="alert ${alert.severity}">
                        <div class="alert-header">
                            <span class="alert-type">${alert.type.replace('_', ' ').toUpperCase()}</span>
                            <span class="alert-severity severity-${alert.severity}">${alert.severity}</span>
                        </div>
                        <div class="alert-message">${alert.message}</div>
                        <div class="alert-timestamp">${new Date(alert.timestamp).toLocaleString()}</div>
                        <button class="resolve-btn" onclick="resolveAlert('${alert.id}')">Resolve</button>
                    </div>
                `).join('');
            }
            
            function addAlert(alert) {
                const container = document.getElementById('alertsContainer');
                const alertHtml = `
                    <div class="alert ${alert.severity}">
                        <div class="alert-header">
                            <span class="alert-type">${alert.type.replace('_', ' ').toUpperCase()}</span>
                            <span class="alert-severity severity-${alert.severity}">${alert.severity}</span>
                        </div>
                        <div class="alert-message">${alert.message}</div>
                        <div class="alert-timestamp">${new Date(alert.timestamp).toLocaleString()}</div>
                        <button class="resolve-btn" onclick="resolveAlert('${alert.id}')">Resolve</button>
                    </div>
                `;
                container.insertAdjacentHTML('afterbegin', alertHtml);
            }
            
            async function resolveAlert(alertId) {
                try {
                    const response = await fetch(`/monitor/alerts/${alertId}/resolve`, {
                        method: 'POST'
                    });
                    
                    if (response.ok) {
                        // Remove alert from UI
                        const alertElement = document.querySelector(`[onclick="resolveAlert('${alertId}')"]`).closest('.alert');
                        alertElement.remove();
                    }
                } catch (error) {
                    console.error('Error resolving alert:', error);
                }
            }
            
            // Initialize dashboard
            connectWebSocket();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(monitor_app, host="127.0.0.1", port=8005)

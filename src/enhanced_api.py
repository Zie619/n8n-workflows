#!/usr/bin/env python3
"""
n8n工作流仓库增强API模块
高级功能、分析和性能优化
"""

import sqlite3
import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
import uvicorn

# 导入社区功能模块
from community_features import CommunityFeatures, create_community_api_endpoints

class WorkflowSearchRequest(BaseModel):
    """工作流搜索请求模型"""
    query: str  # 搜索查询字符串
    categories: Optional[List[str]] = None  # 可选的分类列表
    trigger_types: Optional[List[str]] = None  # 可选的触发器类型列表
    complexity_levels: Optional[List[str]] = None  # 可选的复杂度级别列表
    integrations: Optional[List[str]] = None  # 可选的集成列表
    min_rating: Optional[float] = None  # 可选的最低评分
    limit: int = 20  # 返回结果数量限制
    offset: int = 0  # 结果偏移量

class WorkflowRecommendationRequest(BaseModel):
    """工作流推荐请求模型"""
    user_interests: List[str]  # 用户兴趣列表
    viewed_workflows: Optional[List[str]] = None  # 可选的已查看工作流列表
    preferred_complexity: Optional[str] = None  # 可选的首选复杂度
    limit: int = 10  # 返回结果数量限制

class AnalyticsRequest(BaseModel):
    """分析请求模型"""
    date_range: str  # 日期范围："7d"、"30d"、"90d"、"1y"
    metrics: List[str]  # 指标列表：["views"、"downloads"、"ratings"、"searches"]

class EnhancedAPI:
    """具有高级功能的增强API"""
    
    def __init__(self, db_path: str = "workflows.db"):
        """初始化增强API"""
        self.db_path = db_path
        self.community = CommunityFeatures(db_path)
        self.app = FastAPI(
            title="N8N工作流增强API",
            description="具有社区功能的n8n工作流仓库高级API",
            version="2.0.0"
        )
        self._setup_middleware()
        self._setup_routes()
    
    def _setup_middleware(self):
        """设置中间件以提升性能和安全性"""
        # CORS（跨域资源共享）中间件
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Gzip压缩中间件
        self.app.add_middleware(GZipMiddleware, minimum_size=1000)
    
    def _setup_routes(self):
        """设置API路由"""
        
        # 核心工作流端点
        @self.app.get("/api/v2/workflows")
        async def get_workflows_enhanced(
            search: Optional[str] = Query(None),
            category: Optional[str] = Query(None),
            trigger_type: Optional[str] = Query(None),
            complexity: Optional[str] = Query(None),
            integration: Optional[str] = Query(None),
            min_rating: Optional[float] = Query(None),
            sort_by: str = Query("name"),
            sort_order: str = Query("asc"),
            limit: int = Query(20, le=100),
            offset: int = Query(0, ge=0)
        ):
            """具有多个过滤器的增强工作流搜索"""
            start_time = time.time()
            
            try:
                workflows = self._search_workflows_enhanced(
                    search=search,
                    category=category,
                    trigger_type=trigger_type,
                    complexity=complexity,
                    integration=integration,
                    min_rating=min_rating,
                    sort_by=sort_by,
                    sort_order=sort_order,
                    limit=limit,
                    offset=offset
                )
                
                response_time = (time.time() - start_time) * 1000
                
                return {
                    "workflows": workflows,
                    "total": len(workflows),
                    "limit": limit,
                    "offset": offset,
                    "response_time_ms": round(response_time, 2),
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/api/v2/workflows/search")
        async def advanced_workflow_search(request: WorkflowSearchRequest):
            """具有复杂查询的高级工作流搜索"""
            start_time = time.time()
            
            try:
                results = self._advanced_search(request)
                response_time = (time.time() - start_time) * 1000
                
                return {
                    "results": results,
                    "total": len(results),
                    "query": request.dict(),
                    "response_time_ms": round(response_time, 2),
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/api/v2/workflows/{workflow_id}")
        async def get_workflow_enhanced(
            workflow_id: str,
            include_stats: bool = Query(True),
            include_ratings: bool = Query(True),
            include_related: bool = Query(True)
        ):
            """获取详细的工作流信息"""
            try:
                workflow_data = self._get_workflow_details(
                    workflow_id, include_stats, include_ratings, include_related
                )
                
                if not workflow_data:
                    raise HTTPException(status_code=404, detail="Workflow not found")
                
                return workflow_data
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # 推荐端点
        @self.app.post("/api/v2/recommendations")
        async def get_workflow_recommendations(request: WorkflowRecommendationRequest):
            """获取个性化工作流推荐"""
            try:
                recommendations = self._get_recommendations(request)
                return {
                    "recommendations": recommendations,
                    "user_profile": request.dict(),
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/api/v2/recommendations/trending")
        async def get_trending_workflows(limit: int = Query(10, le=50)):
            """基于最近活动获取热门工作流"""
            try:
                trending = self._get_trending_workflows(limit)
                return {
                    "trending": trending,
                    "limit": limit,
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # 分析端点
        @self.app.get("/api/v2/analytics/overview")
        async def get_analytics_overview():
            """获取分析概览"""
            try:
                overview = self._get_analytics_overview()
                return overview
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/api/v2/analytics/custom")
        async def get_custom_analytics(request: AnalyticsRequest):
            """获取自定义分析数据"""
            try:
                analytics = self._get_custom_analytics(request)
                return analytics
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # 性能监控
        @self.app.get("/api/v2/health")
        async def health_check():
            """具有性能指标的健康检查"""
            try:
                health_data = self._get_health_status()
                return health_data
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # 添加社区端点
        create_community_api_endpoints(self.app)
    
    def _search_workflows_enhanced(self, **kwargs) -> List[Dict]:
        """具有多个过滤器的增强工作流搜索"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 构建动态查询
        query_parts = ["SELECT w.*, ws.average_rating, ws.total_ratings"]
        query_parts.append("FROM workflows w")
        query_parts.append("LEFT JOIN workflow_stats ws ON w.filename = ws.workflow_id")
        
        conditions = []
        params = []
        
        # 应用过滤器
        if kwargs.get('search'):
            conditions.append("(w.name LIKE ? OR w.description LIKE ? OR w.integrations LIKE ?)")
            search_term = f"%{kwargs['search']}%"
            params.extend([search_term, search_term, search_term])
        
        if kwargs.get('category'):
            conditions.append("w.category = ?")
            params.append(kwargs['category'])
        
        if kwargs.get('trigger_type'):
            conditions.append("w.trigger_type = ?")
            params.append(kwargs['trigger_type'])
        
        if kwargs.get('complexity'):
            conditions.append("w.complexity = ?")
            params.append(kwargs['complexity'])
        
        if kwargs.get('integration'):
            conditions.append("w.integrations LIKE ?")
            params.append(f"%{kwargs['integration']}%")
        
        if kwargs.get('min_rating'):
            conditions.append("ws.average_rating >= ?")
            params.append(kwargs['min_rating'])
        
        # 将条件添加到查询
        if conditions:
            query_parts.append("WHERE " + " AND ".join(conditions))
        
        # 添加排序
        sort_by = kwargs.get('sort_by', 'name')
        sort_order = kwargs.get('sort_order', 'asc').upper()
        query_parts.append(f"ORDER BY {sort_by} {sort_order}")
        
        # 添加分页
        query_parts.append("LIMIT ? OFFSET ?")
        params.extend([kwargs.get('limit', 20), kwargs.get('offset', 0)])
        
        # 执行查询
        query = " ".join(query_parts)
        cursor.execute(query, params)
        
        workflows = []
        for row in cursor.fetchall():
            workflows.append({
                'filename': row[0],
                'name': row[1],
                'workflow_id': row[2],
                'active': bool(row[3]),
                'description': row[4],
                'trigger_type': row[5],
                'complexity': row[6],
                'node_count': row[7],
                'integrations': row[8],
                'tags': row[9],
                'created_at': row[10],
                'updated_at': row[11],
                'file_hash': row[12],
                'file_size': row[13],
                'analyzed_at': row[14],
                'average_rating': row[15],
                'total_ratings': row[16]
            })
        
        conn.close()
        return workflows
    
    def _advanced_search(self, request: WorkflowSearchRequest) -> List[Dict]:
        """具有复杂查询的高级搜索"""
        # 高级搜索逻辑的实现
        # 这将包括语义搜索、模糊匹配等
        return self._search_workflows_enhanced(
            search=request.query,
            category=request.categories[0] if request.categories else None,
            trigger_type=request.trigger_types[0] if request.trigger_types else None,
            complexity=request.complexity_levels[0] if request.complexity_levels else None,
            limit=request.limit,
            offset=request.offset
        )
    
    def _get_workflow_details(self, workflow_id: str, include_stats: bool, 
                            include_ratings: bool, include_related: bool) -> Dict:
        """获取详细的工作流信息"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 获取基本工作流数据
        cursor.execute("SELECT * FROM workflows WHERE filename = ?", (workflow_id,))
        workflow_row = cursor.fetchone()
        
        if not workflow_row:
            conn.close()
            return None
        
        workflow_data = {
            'filename': workflow_row[0],
            'name': workflow_row[1],
            'workflow_id': workflow_row[2],
            'active': bool(workflow_row[3]),
            'description': workflow_row[4],
            'trigger_type': workflow_row[5],
            'complexity': workflow_row[6],
            'node_count': workflow_row[7],
            'integrations': workflow_row[8],
            'tags': workflow_row[9],
            'created_at': workflow_row[10],
            'updated_at': workflow_row[11],
            'file_hash': workflow_row[12],
            'file_size': workflow_row[13],
            'analyzed_at': workflow_row[14]
        }
        
        # 如果请求，添加统计信息
        if include_stats:
            stats = self.community.get_workflow_stats(workflow_id)
            workflow_data['stats'] = stats.__dict__ if stats else None
        
        # 如果请求，添加评分
        if include_ratings:
            ratings = self.community.get_workflow_ratings(workflow_id, 5)
            workflow_data['ratings'] = [rating.__dict__ for rating in ratings]
        
        # 如果请求，添加相关工作流
        if include_related:
            related = self._get_related_workflows(workflow_id)
            workflow_data['related_workflows'] = related
        
        conn.close()
        return workflow_data
    
    def _get_recommendations(self, request: WorkflowRecommendationRequest) -> List[Dict]:
        """获取个性化工作流推荐"""
        # 推荐算法的实现
        # 这将使用协同过滤、基于内容的过滤等
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 基于用户兴趣的简单推荐
        recommendations = []
        for interest in request.user_interests:
            cursor.execute("""
                SELECT * FROM workflows 
                WHERE integrations LIKE ? OR name LIKE ? OR description LIKE ?
                LIMIT 5
            """, (f"%{interest}%", f"%{interest}%", f"%{interest}%"))
            
            for row in cursor.fetchall():
                recommendations.append({
                    'filename': row[0],
                    'name': row[1],
                    'description': row[4],
                    'reason': f"Matches your interest in {interest}"
                })
        
        conn.close()
        return recommendations[:request.limit]
    
    def _get_trending_workflows(self, limit: int) -> List[Dict]:
        """基于最近活动获取热门工作流"""
        return self.community.get_most_popular_workflows(limit)
    
    def _get_analytics_overview(self) -> Dict:
        """获取分析概览"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 工作流总数
        cursor.execute("SELECT COUNT(*) FROM workflows")
        total_workflows = cursor.fetchone()[0]
        
        # 活跃工作流数
        cursor.execute("SELECT COUNT(*) FROM workflows WHERE active = 1")
        active_workflows = cursor.fetchone()[0]
        
        # 分类统计
        cursor.execute("SELECT category, COUNT(*) FROM workflows GROUP BY category")
        categories = dict(cursor.fetchall())
        
        # 集成统计
        cursor.execute("SELECT COUNT(DISTINCT integrations) FROM workflows")
        unique_integrations = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_workflows': total_workflows,
            'active_workflows': active_workflows,
            'categories': categories,
            'unique_integrations': unique_integrations,
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_custom_analytics(self, request: AnalyticsRequest) -> Dict:
        """获取自定义分析数据"""
        # 自定义分析的实现
        return {
            'date_range': request.date_range,
            'metrics': request.metrics,
            'data': {},  # 实际分析数据的占位符
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_health_status(self) -> Dict:
        """获取健康状态和性能指标"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 数据库健康状态
        cursor.execute("SELECT COUNT(*) FROM workflows")
        total_workflows = cursor.fetchone()[0]
        
        # 性能测试
        start_time = time.time()
        cursor.execute("SELECT COUNT(*) FROM workflows WHERE active = 1")
        active_count = cursor.fetchone()[0]
        query_time = (time.time() - start_time) * 1000
        
        conn.close()
        
        return {
            'status': 'healthy',
            'database': {
                'total_workflows': total_workflows,
                'active_workflows': active_count,
                'connection_status': 'connected'
            },
            'performance': {
                'query_time_ms': round(query_time, 2),
                'response_time_target': '<100ms',
                'status': 'good' if query_time < 100 else 'slow'
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_related_workflows(self, workflow_id: str, limit: int = 5) -> List[Dict]:
        """基于相似的集成或分类获取相关工作流"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 获取当前工作流详情
        cursor.execute("SELECT integrations, category FROM workflows WHERE filename = ?", (workflow_id,))
        current_workflow = cursor.fetchone()
        
        if not current_workflow:
            conn.close()
            return []
        
        current_integrations = current_workflow[0] or ""
        current_category = current_workflow[1] or ""
        
        # 查找工作流
        cursor.execute("""
            SELECT filename, name, description FROM workflows 
            WHERE filename != ? 
            AND (integrations LIKE ? OR category = ?)
            LIMIT ?
        """, (workflow_id, f"%{current_integrations[:50]}%", current_category, limit))
        
        related = []
        for row in cursor.fetchall():
            related.append({
                'filename': row[0],
                'name': row[1],
                'description': row[2]
            })
        
        conn.close()
        return related
    
    def run(self, host: str = "127.0.0.1", port: int = 8000, debug: bool = False):
        """运行增强API服务器"""
        uvicorn.run(
            self.app,
            host=host,
            port=port,
            log_level="debug" if debug else "info"
        )

if __name__ == "__main__":
    # 初始化并运行增强API
    api = EnhancedAPI()
    print("🚀 正在启动增强N8N工作流API...")
    print("📊 功能：高级搜索、推荐、分析、社区功能")
    print("🌐 API文档：http://127.0.0.1:8000/docs")
    
    api.run(debug=True)

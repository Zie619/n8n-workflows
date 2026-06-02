#!/usr/bin/env python3
"""
Enhanced API Module for n8n Workflows Repository
Advanced features, analytics, and performance optimizations
"""

import sqlite3
import time
from datetime import datetime
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
import uvicorn

# Import community features
from community_features import CommunityFeatures, create_community_api_endpoints


class WorkflowSearchRequest(BaseModel):
    """Workflow search request model"""

    query: str
    categories: Optional[List[str]] = None
    trigger_types: Optional[List[str]] = None
    complexity_levels: Optional[List[str]] = None
    integrations: Optional[List[str]] = None
    min_rating: Optional[float] = None
    limit: int = 20
    offset: int = 0


class WorkflowRecommendationRequest(BaseModel):
    """Workflow recommendation request model"""

    user_interests: List[str]
    viewed_workflows: Optional[List[str]] = None
    preferred_complexity: Optional[str] = None
    limit: int = 10


class AnalyticsRequest(BaseModel):
    """Analytics request model"""

    date_range: str  # "7d", "30d", "90d", "1y"
    metrics: List[str]  # ["views", "downloads", "ratings", "searches"]


class EnhancedAPI:
    """Enhanced API with advanced features"""

    def __init__(self, db_path: str = "workflows.db"):
        """Initialize enhanced API"""
        self.db_path = db_path
        self.community = CommunityFeatures(db_path)
        self.app = FastAPI(
            title="N8N Workflows Enhanced API",
            description="Advanced API for n8n workflows repository with community features",
            version="2.0.0",
        )
        self._setup_middleware()
        self._setup_routes()

    def _setup_middleware(self):
        """Setup middleware for performance and security"""
        # CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Gzip compression
        self.app.add_middleware(GZipMiddleware, minimum_size=1000)

    def _setup_routes(self):
        """Setup API routes"""

        # Core workflow endpoints
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
            offset: int = Query(0, ge=0),
        ):
            """Enhanced workflow search with multiple filters"""
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
                    offset=offset,
                )

                response_time = (time.time() - start_time) * 1000

                return {
                    "workflows": workflows,
                    "total": len(workflows),
                    "limit": limit,
                    "offset": offset,
                    "response_time_ms": round(response_time, 2),
                    "timestamp": datetime.now().isoformat(),
                }

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.post("/api/v2/workflows/search")
        async def advanced_workflow_search(request: WorkflowSearchRequest):
            """Advanced workflow search with complex queries"""
            start_time = time.time()

            try:
                results = self._advanced_search(request)
                response_time = (time.time() - start_time) * 1000

                return {
                    "results": results,
                    "total": len(results),
                    "query": request.dict(),
                    "response_time_ms": round(response_time, 2),
                    "timestamp": datetime.now().isoformat(),
                }

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.get("/api/v2/workflows/{workflow_id}")
        async def get_workflow_enhanced(
            workflow_id: str,
            include_stats: bool = Query(True),
            include_ratings: bool = Query(True),
            include_related: bool = Query(True),
        ):
            """Get detailed workflow information"""
            try:
                workflow_data = self._get_workflow_details(
                    workflow_id, include_stats, include_ratings, include_related
                )

                if not workflow_data:
                    raise HTTPException(status_code=404, detail="Workflow not found")

                return workflow_data

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        # Recommendation endpoints
        @self.app.post("/api/v2/recommendations")
        async def get_workflow_recommendations(request: WorkflowRecommendationRequest):
            """Get personalized workflow recommendations"""
            try:
                recommendations = self._get_recommendations(request)
                return {
                    "recommendations": recommendations,
                    "user_profile": request.dict(),
                    "timestamp": datetime.now().isoformat(),
                }

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.get("/api/v2/recommendations/trending")
        async def get_trending_workflows(limit: int = Query(10, le=50)):
            """Get trending workflows based on recent activity"""
            try:
                trending = self._get_trending_workflows(limit)
                return {
                    "trending": trending,
                    "limit": limit,
                    "timestamp": datetime.now().isoformat(),
                }

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        # Analytics endpoints
        @self.app.get("/api/v2/analytics/overview")
        async def get_analytics_overview():
            """Get analytics overview"""
            try:
                overview = self._get_analytics_overview()
                return overview

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.post("/api/v2/analytics/custom")
        async def get_custom_analytics(request: AnalyticsRequest):
            """Get custom analytics data"""
            try:
                analytics = self._get_custom_analytics(request)
                return analytics

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        # Performance monitoring
        @self.app.get("/api/v2/health")
        async def health_check():
            """Health check with performance metrics"""
            try:
                health_data = self._get_health_status()
                return health_data

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        # Add community endpoints
        create_community_api_endpoints(self.app)

    def _search_workflows_enhanced(self, **kwargs) -> List[Dict]:
        """Enhanced workflow search with multiple filters"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Build dynamic query
        query_parts = ["SELECT w.*, ws.average_rating, ws.total_ratings"]
        query_parts.append("FROM workflows w")
        query_parts.append("LEFT JOIN workflow_stats ws ON w.filename = ws.workflow_id")

        conditions = []
        params = []

        # Apply filters
        if kwargs.get("search"):
            conditions.append(
                "(w.name LIKE ? OR w.description LIKE ? OR w.integrations LIKE ?)"
            )
            search_term = f"%{kwargs['search']}%"
            params.extend([search_term, search_term, search_term])

        if kwargs.get("category"):
            conditions.append("w.category = ?")
            params.append(kwargs["category"])

        if kwargs.get("trigger_type"):
            conditions.append("w.trigger_type = ?")
            params.append(kwargs["trigger_type"])

        if kwargs.get("complexity"):
            conditions.append("w.complexity = ?")
            params.append(kwargs["complexity"])

        if kwargs.get("integration"):
            conditions.append("w.integrations LIKE ?")
            params.append(f"%{kwargs['integration']}%")

        if kwargs.get("min_rating"):
            conditions.append("ws.average_rating >= ?")
            params.append(kwargs["min_rating"])

        # Add conditions to query
        if conditions:
            query_parts.append("WHERE " + " AND ".join(conditions))

        # Add sorting
        sort_by = kwargs.get("sort_by", "name")
        sort_order = kwargs.get("sort_order", "asc").upper()
        query_parts.append(f"ORDER BY {sort_by} {sort_order}")

        # Add pagination
        query_parts.append("LIMIT ? OFFSET ?")
        params.extend([kwargs.get("limit", 20), kwargs.get("offset", 0)])

        # Execute query
        query = " ".join(query_parts)
        cursor.execute(query, params)

        workflows = []
        for row in cursor.fetchall():
            workflows.append(
                {
                    "filename": row[0],
                    "name": row[1],
                    "workflow_id": row[2],
                    "active": bool(row[3]),
                    "description": row[4],
                    "trigger_type": row[5],
                    "complexity": row[6],
                    "node_count": row[7],
                    "integrations": row[8],
                    "tags": row[9],
                    "created_at": row[10],
                    "updated_at": row[11],
                    "file_hash": row[12],
                    "file_size": row[13],
                    "analyzed_at": row[14],
                    "average_rating": row[15],
                    "total_ratings": row[16],
                }
            )

        conn.close()
        return workflows

    def _advanced_search(self, request: WorkflowSearchRequest) -> List[Dict]:
        """Advanced search with complex queries"""
        # Implementation for advanced search logic
        # This would include semantic search, fuzzy matching, etc.
        return self._search_workflows_enhanced(
            search=request.query,
            category=request.categories[0] if request.categories else None,
            trigger_type=request.trigger_types[0] if request.trigger_types else None,
            complexity=request.complexity_levels[0]
            if request.complexity_levels
            else None,
            limit=request.limit,
            offset=request.offset,
        )

    def _get_workflow_details(
        self,
        workflow_id: str,
        include_stats: bool,
        include_ratings: bool,
        include_related: bool,
    ) -> Dict:
        """Get detailed workflow information"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get basic workflow data
        cursor.execute("SELECT * FROM workflows WHERE filename = ?", (workflow_id,))
        workflow_row = cursor.fetchone()

        if not workflow_row:
            conn.close()
            return None

        workflow_data = {
            "filename": workflow_row[0],
            "name": workflow_row[1],
            "workflow_id": workflow_row[2],
            "active": bool(workflow_row[3]),
            "description": workflow_row[4],
            "trigger_type": workflow_row[5],
            "complexity": workflow_row[6],
            "node_count": workflow_row[7],
            "integrations": workflow_row[8],
            "tags": workflow_row[9],
            "created_at": workflow_row[10],
            "updated_at": workflow_row[11],
            "file_hash": workflow_row[12],
            "file_size": workflow_row[13],
            "analyzed_at": workflow_row[14],
        }

        # Add statistics if requested
        if include_stats:
            stats = self.community.get_workflow_stats(workflow_id)
            workflow_data["stats"] = stats.__dict__ if stats else None

        # Add ratings if requested
        if include_ratings:
            ratings = self.community.get_workflow_ratings(workflow_id, 5)
            workflow_data["ratings"] = [rating.__dict__ for rating in ratings]

        # Add related workflows if requested
        if include_related:
            related = self._get_related_workflows(workflow_id)
            workflow_data["related_workflows"] = related

        conn.close()
        return workflow_data

    def _get_recommendations(
        self, request: WorkflowRecommendationRequest
    ) -> List[Dict]:
        """Get personalized workflow recommendations"""
        # Implementation for recommendation algorithm
        # This would use collaborative filtering, content-based filtering, etc.
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Simple recommendation based on user interests
        recommendations = []
        for interest in request.user_interests:
            cursor.execute(
                """
                SELECT * FROM workflows 
                WHERE integrations LIKE ? OR name LIKE ? OR description LIKE ?
                LIMIT 5
            """,
                (f"%{interest}%", f"%{interest}%", f"%{interest}%"),
            )

            for row in cursor.fetchall():
                recommendations.append(
                    {
                        "filename": row[0],
                        "name": row[1],
                        "description": row[4],
                        "reason": f"Matches your interest in {interest}",
                    }
                )

        conn.close()
        return recommendations[: request.limit]

    def _get_trending_workflows(self, limit: int) -> List[Dict]:
        """Get trending workflows based on recent activity"""
        return self.community.get_most_popular_workflows(limit)

    def _get_analytics_overview(self) -> Dict:
        """Get analytics overview"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Total workflows
        cursor.execute("SELECT COUNT(*) FROM workflows")
        total_workflows = cursor.fetchone()[0]

        # Active workflows
        cursor.execute("SELECT COUNT(*) FROM workflows WHERE active = 1")
        active_workflows = cursor.fetchone()[0]

        # Categories
        cursor.execute("SELECT category, COUNT(*) FROM workflows GROUP BY category")
        categories = dict(cursor.fetchall())

        # Integrations
        cursor.execute("SELECT COUNT(DISTINCT integrations) FROM workflows")
        unique_integrations = cursor.fetchone()[0]

        conn.close()

        return {
            "total_workflows": total_workflows,
            "active_workflows": active_workflows,
            "categories": categories,
            "unique_integrations": unique_integrations,
            "timestamp": datetime.now().isoformat(),
        }

    def _get_custom_analytics(self, request: AnalyticsRequest) -> Dict:
        """Get custom analytics data"""
        # Implementation for custom analytics
        return {
            "date_range": request.date_range,
            "metrics": request.metrics,
            "data": {},  # Placeholder for actual analytics data
            "timestamp": datetime.now().isoformat(),
        }

    def _get_health_status(self) -> Dict:
        """Get health status and performance metrics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Database health
        cursor.execute("SELECT COUNT(*) FROM workflows")
        total_workflows = cursor.fetchone()[0]

        # Performance test
        start_time = time.time()
        cursor.execute("SELECT COUNT(*) FROM workflows WHERE active = 1")
        active_count = cursor.fetchone()[0]
        query_time = (time.time() - start_time) * 1000

        conn.close()

        return {
            "status": "healthy",
            "database": {
                "total_workflows": total_workflows,
                "active_workflows": active_count,
                "connection_status": "connected",
            },
            "performance": {
                "query_time_ms": round(query_time, 2),
                "response_time_target": "<100ms",
                "status": "good" if query_time < 100 else "slow",
            },
            "timestamp": datetime.now().isoformat(),
        }

    def _get_related_workflows(self, workflow_id: str, limit: int = 5) -> List[Dict]:
        """Get related workflows based on similar integrations or categories"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get current workflow details
        cursor.execute(
            "SELECT integrations, category FROM workflows WHERE filename = ?",
            (workflow_id,),
        )
        current_workflow = cursor.fetchone()

        if not current_workflow:
            conn.close()
            return []

        current_integrations = current_workflow[0] or ""
        current_category = current_workflow[1] or ""

        # Find related workflows
        cursor.execute(
            """
            SELECT filename, name, description FROM workflows 
            WHERE filename != ? 
            AND (integrations LIKE ? OR category = ?)
            LIMIT ?
        """,
            (workflow_id, f"%{current_integrations[:50]}%", current_category, limit),
        )

        related = []
        for row in cursor.fetchall():
            related.append({"filename": row[0], "name": row[1], "description": row[2]})

        conn.close()
        return related

    def run(self, host: str = "127.0.0.1", port: int = 8000, debug: bool = False):
        """Run the enhanced API server"""
        uvicorn.run(
            self.app, host=host, port=port, log_level="debug" if debug else "info"
        )


if __name__ == "__main__":
    # Initialize and run enhanced API
    api = EnhancedAPI()
    print("🚀 Starting Enhanced N8N Workflows API...")
    print(
        "📊 Features: Advanced search, recommendations, analytics, community features"
    )
    print("🌐 API Documentation: http://127.0.0.1:8000/docs")

    api.run(debug=True)

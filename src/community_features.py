#!/usr/bin/env python3
"""
N8N 工作流仓库社区功能模块
实现评分、评论和社交功能
"""

import sqlite3
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class WorkflowRating:
    """工作流评分数据结构"""
    workflow_id: str
    user_id: str
    rating: int  # 1-5 星
    review: Optional[str] = None
    helpful_votes: int = 0
    created_at: datetime = None
    updated_at: datetime = None

@dataclass
class WorkflowStats:
    """工作流统计数据"""
    workflow_id: str
    total_ratings: int
    average_rating: float
    total_reviews: int
    total_views: int
    total_downloads: int
    last_updated: datetime

class CommunityFeatures:
    """工作流仓库的社区功能管理器"""
    
    def __init__(self, db_path: str = "workflows.db"):
        """使用数据库连接初始化社区功能"""
        self.db_path = db_path
        self.init_community_tables()
    
    def init_community_tables(self):
        """初始化社区功能数据库表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 工作流评分和评论
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workflow_ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                workflow_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                rating INTEGER CHECK(rating >= 1 AND rating <= 5),
                review TEXT,
                helpful_votes INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(workflow_id, user_id)
            )
        """)
        
        # 工作流使用统计
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workflow_stats (
                workflow_id TEXT PRIMARY KEY,
                total_ratings INTEGER DEFAULT 0,
                average_rating REAL DEFAULT 0.0,
                total_reviews INTEGER DEFAULT 0,
                total_views INTEGER DEFAULT 0,
                total_downloads INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 用户资料
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profiles (
                user_id TEXT PRIMARY KEY,
                username TEXT,
                display_name TEXT,
                email TEXT,
                avatar_url TEXT,
                bio TEXT,
                github_url TEXT,
                website_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 工作流集合（用户收藏）
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workflow_collections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                collection_name TEXT NOT NULL,
                workflow_ids TEXT, -- 工作流 ID 的 JSON 数组
                is_public BOOLEAN DEFAULT FALSE,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 工作流评论
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workflow_comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                workflow_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                parent_id INTEGER, -- 用于线程评论
                comment TEXT NOT NULL,
                helpful_votes INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_rating(self, workflow_id: str, user_id: str, rating: int, review: str = None) -> bool:
        """添加或更新工作流评分和评论"""
        if not (1 <= rating <= 5):
            raise ValueError("评分必须在 1 到 5 之间")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # 插入或更新评分
            cursor.execute("""
                INSERT OR REPLACE INTO workflow_ratings 
                (workflow_id, user_id, rating, review, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (workflow_id, user_id, rating, review))
            
            # 更新工作流统计
            self._update_workflow_stats(workflow_id)
            
            conn.commit()
            return True
            
        except Exception as e:
            print(f"添加评分时出错：{e}")
            return False
        finally:
            conn.close()
    
    def get_workflow_ratings(self, workflow_id: str, limit: int = 10) -> List[WorkflowRating]:
        """获取工作流的评分和评论"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT workflow_id, user_id, rating, review, helpful_votes, created_at, updated_at
            FROM workflow_ratings 
            WHERE workflow_id = ? 
            ORDER BY helpful_votes DESC, created_at DESC 
            LIMIT ?
        """, (workflow_id, limit))
        
        ratings = []
        for row in cursor.fetchall():
            ratings.append(WorkflowRating(
                workflow_id=row[0],
                user_id=row[1],
                rating=row[2],
                review=row[3],
                helpful_votes=row[4],
                created_at=datetime.fromisoformat(row[5]) if row[5] else None,
                updated_at=datetime.fromisoformat(row[6]) if row[6] else None
            ))
        
        conn.close()
        return ratings
    
    def get_workflow_stats(self, workflow_id: str) -> Optional[WorkflowStats]:
        """获取工作流的全面统计数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT workflow_id, total_ratings, average_rating, total_reviews, 
                   total_views, total_downloads, last_updated
            FROM workflow_stats 
            WHERE workflow_id = ?
        """, (workflow_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return WorkflowStats(
                workflow_id=row[0],
                total_ratings=row[1],
                average_rating=row[2],
                total_reviews=row[3],
                total_views=row[4],
                total_downloads=row[5],
                last_updated=datetime.fromisoformat(row[6]) if row[6] else None
            )
        return None
    
    def increment_view(self, workflow_id: str):
        """增加工作流的浏览计数"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR IGNORE INTO workflow_stats (workflow_id, total_views)
            VALUES (?, 1)
        """, (workflow_id,))
        
        cursor.execute("""
            UPDATE workflow_stats 
            SET total_views = total_views + 1, last_updated = CURRENT_TIMESTAMP
            WHERE workflow_id = ?
        """, (workflow_id,))
        
        conn.commit()
        conn.close()
    
    def increment_download(self, workflow_id: str):
        """增加工作流的下载计数"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR IGNORE INTO workflow_stats (workflow_id, total_downloads)
            VALUES (?, 1)
        """, (workflow_id,))
        
        cursor.execute("""
            UPDATE workflow_stats 
            SET total_downloads = total_downloads + 1, last_updated = CURRENT_TIMESTAMP
            WHERE workflow_id = ?
        """, (workflow_id,))
        
        conn.commit()
        conn.close()
    
    def get_top_rated_workflows(self, limit: int = 10) -> List[Dict]:
        """获取评分最高的工作流"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT w.filename, w.name, w.description, ws.average_rating, ws.total_ratings
            FROM workflows w
            JOIN workflow_stats ws ON w.filename = ws.workflow_id
            WHERE ws.total_ratings >= 3
            ORDER BY ws.average_rating DESC, ws.total_ratings DESC
            LIMIT ?
        """, (limit,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'filename': row[0],
                'name': row[1],
                'description': row[2],
                'average_rating': row[3],
                'total_ratings': row[4]
            })
        
        conn.close()
        return results
    
    def get_most_popular_workflows(self, limit: int = 10) -> List[Dict]:
        """根据浏览量和下载量获取最受欢迎的工作流"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT w.filename, w.name, w.description, ws.total_views, ws.total_downloads
            FROM workflows w
            LEFT JOIN workflow_stats ws ON w.filename = ws.workflow_id
            ORDER BY (ws.total_views + ws.total_downloads) DESC
            LIMIT ?
        """, (limit,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'filename': row[0],
                'name': row[1],
                'description': row[2],
                'total_views': row[3] or 0,
                'total_downloads': row[4] or 0
            })
        
        conn.close()
        return results
    
    def create_collection(self, user_id: str, collection_name: str, workflow_ids: List[str], 
                         is_public: bool = False, description: str = None) -> bool:
        """创建工作流集合"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO workflow_collections 
                (user_id, collection_name, workflow_ids, is_public, description)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, collection_name, json.dumps(workflow_ids), is_public, description))
            
            conn.commit()
            return True
            
        except Exception as e:
            print(f"创建集合时出错：{e}")
            return False
        finally:
            conn.close()
    
    def get_user_collections(self, user_id: str) -> List[Dict]:
        """获取用户的集合"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, collection_name, workflow_ids, is_public, description, created_at
            FROM workflow_collections 
            WHERE user_id = ?
            ORDER BY created_at DESC
        """, (user_id,))
        
        collections = []
        for row in cursor.fetchall():
            collections.append({
                'id': row[0],
                'name': row[1],
                'workflow_ids': json.loads(row[2]) if row[2] else [],
                'is_public': bool(row[3]),
                'description': row[4],
                'created_at': row[5]
            })
        
        conn.close()
        return collections
    
    def _update_workflow_stats(self, workflow_id: str):
        """评分变更后更新工作流统计数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Calculate new statistics
        cursor.execute("""
            SELECT COUNT(*), AVG(rating), COUNT(CASE WHEN review IS NOT NULL THEN 1 END)
            FROM workflow_ratings 
            WHERE workflow_id = ?
        """, (workflow_id,))
        
        total_ratings, avg_rating, total_reviews = cursor.fetchone()
        
        # Update or insert statistics
        cursor.execute("""
            INSERT OR REPLACE INTO workflow_stats 
            (workflow_id, total_ratings, average_rating, total_reviews, last_updated)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, (workflow_id, total_ratings or 0, avg_rating or 0.0, total_reviews or 0))
        
        conn.commit()
        conn.close()

# 示例用法和 API 端点
def create_community_api_endpoints(app):
    """向 FastAPI 应用添加社区功能端点"""
    community = CommunityFeatures()
    
    @app.post("/api/workflows/{workflow_id}/rate")
    async def rate_workflow(workflow_id: str, rating_data: dict):
        """为工作流评分"""
        try:
            success = community.add_rating(
                workflow_id=workflow_id,
                user_id=rating_data.get('user_id', 'anonymous'),  # 匿名用户
                rating=rating_data['rating'],
                review=rating_data.get('review')
            )
            return {"success": success}
        except Exception as e:
            return {"error": str(e)}
    
    @app.get("/api/workflows/{workflow_id}/ratings")
    async def get_workflow_ratings(workflow_id: str, limit: int = 10):
        """获取工作流评分和评论"""
        ratings = community.get_workflow_ratings(workflow_id, limit)
        return {"ratings": ratings}
    
    @app.get("/api/workflows/{workflow_id}/stats")
    async def get_workflow_stats(workflow_id: str):
        """获取工作流统计数据"""
        stats = community.get_workflow_stats(workflow_id)
        return {"stats": stats}
    
    @app.get("/api/workflows/top-rated")
    async def get_top_rated_workflows(limit: int = 10):
        """获取评分最高的工作流"""
        workflows = community.get_top_rated_workflows(limit)
        return {"workflows": workflows}
    
    @app.get("/api/workflows/most-popular")
    async def get_most_popular_workflows(limit: int = 10):
        """获取最受欢迎的工作流"""
        workflows = community.get_most_popular_workflows(limit)
        return {"workflows": workflows}
    
    @app.post("/api/workflows/{workflow_id}/view")
    async def track_workflow_view(workflow_id: str):
        """记录工作流浏览"""
        community.increment_view(workflow_id)
        return {"success": True}
    
    @app.post("/api/workflows/{workflow_id}/download")
    async def track_workflow_download(workflow_id: str):
        """记录工作流下载"""
        community.increment_download(workflow_id)
        return {"success": True}

if __name__ == "__main__":
    # 初始化社区功能
    community = CommunityFeatures()
    print("✅ 社区功能初始化成功！")
    
    # 示例：添加评分
    # community.add_rating("example-workflow.json", "user123", 5, "很棒的工作流！")
    
    # 示例：获取评分最高的工作流
    top_workflows = community.get_top_rated_workflows(5)
    print(f"📊 评分最高的工作流数量：{len(top_workflows)}")

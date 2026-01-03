#!/usr/bin/env python3
"""
快速 N8N 工作流数据库
基于 SQLite 的工作流索引器和搜索引擎，提供即时性能。
"""

import sqlite3
import json
import os
import glob
import datetime
import hashlib
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

class WorkflowDatabase:
    """高性能的 SQLite 数据库，用于工作流元数据和搜索。"""
    
    def __init__(self, db_path: str = None):
        # 如果没有提供路径，则使用环境变量
        if db_path is None:
            db_path = os.environ.get('WORKFLOW_DB_PATH', 'workflows.db')
        self.db_path = db_path
        self.workflows_dir = "workflows"
        self.init_database()
    
    def init_database(self):
        """使用优化的架构和索引初始化 SQLite 数据库。"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL")  # 启用预写日志以提高性能
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA cache_size=10000")
        conn.execute("PRAGMA temp_store=MEMORY")
        
        # 创建主工作流表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS workflows (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                workflow_id TEXT,
                active BOOLEAN DEFAULT 0,
                description TEXT,
                trigger_type TEXT,
                complexity TEXT,
                node_count INTEGER DEFAULT 0,
                integrations TEXT,  -- JSON array
                tags TEXT,         -- JSON array
                created_at TEXT,
                updated_at TEXT,
                file_hash TEXT,
                file_size INTEGER,
                analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 创建用于全文搜索的 FTS5 表
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS workflows_fts USING fts5(
                filename,
                name,
                description,
                integrations,
                tags,
                content=workflows,
                content_rowid=id
            )
        """)
        
        # 创建索引以加快过滤速度
        conn.execute("CREATE INDEX IF NOT EXISTS idx_trigger_type ON workflows(trigger_type)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_complexity ON workflows(complexity)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_active ON workflows(active)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_node_count ON workflows(node_count)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_filename ON workflows(filename)")
        
        # 创建触发器以保持 FTS 表同步
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS workflows_ai AFTER INSERT ON workflows BEGIN
                INSERT INTO workflows_fts(rowid, filename, name, description, integrations, tags)
                VALUES (new.id, new.filename, new.name, new.description, new.integrations, new.tags);
            END
        """)
        
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS workflows_ad AFTER DELETE ON workflows BEGIN
                INSERT INTO workflows_fts(workflows_fts, rowid, filename, name, description, integrations, tags)
                VALUES ('delete', old.id, old.filename, old.name, old.description, old.integrations, old.tags);
            END
        """)
        
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS workflows_au AFTER UPDATE ON workflows BEGIN
                INSERT INTO workflows_fts(workflows_fts, rowid, filename, name, description, integrations, tags)
                VALUES ('delete', old.id, old.filename, old.name, old.description, old.integrations, old.tags);
                INSERT INTO workflows_fts(rowid, filename, name, description, integrations, tags)
                VALUES (new.id, new.filename, new.name, new.description, new.integrations, new.tags);
            END
        """)
        
        conn.commit()
        conn.close()
    
    def get_file_hash(self, file_path: str) -> str:
        """获取文件的 MD5 哈希值用于变更检测。"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def format_workflow_name(self, filename: str) -> str:
        """将文件名转换为可读的工作流名称。"""
        # 移除 .json 扩展名
        name = filename.replace('.json', '')
        
        # 按下划线分割
        parts = name.split('_')
        
        # 如果第一部分只是数字则跳过
        if len(parts) > 1 and parts[0].isdigit():
            parts = parts[1:]
        
        # 将各部分转换为标题大小写并使用空格连接
        readable_parts = []
        for part in parts:
            # 对常见术语进行特殊处理
            if part.lower() == 'http':
                readable_parts.append('HTTP')
            elif part.lower() == 'api':
                readable_parts.append('API')
            elif part.lower() == 'webhook':
                readable_parts.append('Webhook')
            elif part.lower() == 'automation':
                readable_parts.append('Automation')
            elif part.lower() == 'automate':
                readable_parts.append('Automate')
            elif part.lower() == 'scheduled':
                readable_parts.append('Scheduled')
            elif part.lower() == 'triggered':
                readable_parts.append('Triggered')
            elif part.lower() == 'manual':
                readable_parts.append('Manual')
            else:
                # 首字母大写
                readable_parts.append(part.capitalize())
        
        return ' '.join(readable_parts)
    
    def analyze_workflow_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """分析单个工作流文件并提取元数据。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"读取 {file_path} 时出错: {str(e)}")
            return None
        
        filename = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        file_hash = self.get_file_hash(file_path)
        
        # 提取基本元数据
        workflow = {
            'filename': filename,
            'name': self.format_workflow_name(filename),
            'workflow_id': data.get('id', ''),
            'active': data.get('active', False),
            'nodes': data.get('nodes', []),
            'connections': data.get('connections', {}),
            'tags': data.get('tags', []),
            'created_at': data.get('createdAt', ''),
            'updated_at': data.get('updatedAt', ''),
            'file_hash': file_hash,
            'file_size': file_size
        }
        
        # 如果 JSON 名称可用且有意义，则使用它，否则使用格式化的文件名
        json_name = data.get('name', '').strip()
        if json_name and json_name != filename.replace('.json', '') and not json_name.startswith('My workflow'):
            workflow['name'] = json_name
        # 如果没有有意义的 JSON 名称，则使用格式化的文件名（已在上面设置）
        
        # 分析节点
        node_count = len(workflow['nodes'])
        workflow['node_count'] = node_count
        
        # 确定复杂度
        if node_count <= 5:
            complexity = 'low'
        elif node_count <= 15:
            complexity = 'medium'
        else:
            complexity = 'high'
        workflow['complexity'] = complexity
        
        # 查找触发器类型和集成
        trigger_type, integrations = self.analyze_nodes(workflow['nodes'])
        workflow['trigger_type'] = trigger_type
        workflow['integrations'] = list(integrations)
        
        # 如果有 JSON 描述则使用，否则生成一个
        json_description = data.get('description', '').strip()
        if json_description:
            workflow['description'] = json_description
        else:
            workflow['description'] = self.generate_description(workflow, trigger_type, integrations)
        
        return workflow
    
    def analyze_nodes(self, nodes: List[Dict]) -> Tuple[str, set]:
        """分析节点以确定触发器类型和集成。"""
        trigger_type = 'Manual'
        integrations = set()
        
        # 增强的服务映射以提高识别率
        service_mappings = {
            # 消息与通信
            'telegram': 'Telegram',
            'telegramTrigger': 'Telegram',
            'discord': 'Discord',
            'slack': 'Slack', 
            'whatsapp': 'WhatsApp',
            'mattermost': 'Mattermost',
            'teams': 'Microsoft Teams',
            'rocketchat': 'Rocket.Chat',
            
            # 电子邮件
            'gmail': 'Gmail',
            'mailjet': 'Mailjet',
            'emailreadimap': 'Email (IMAP)',
            'emailsendsmt': 'Email (SMTP)',
            'outlook': 'Outlook',
            
            # 云存储
            'googledrive': 'Google Drive',
            'googledocs': 'Google Docs',
            'googlesheets': 'Google Sheets',
            'dropbox': 'Dropbox',
            'onedrive': 'OneDrive',
            'box': 'Box',
            
            # 数据库
            'postgres': 'PostgreSQL',
            'mysql': 'MySQL',
            'mongodb': 'MongoDB',
            'redis': 'Redis',
            'airtable': 'Airtable',
            'notion': 'Notion',
            
            # 项目管理
            'jira': 'Jira',
            'github': 'GitHub',
            'gitlab': 'GitLab',
            'trello': 'Trello',
            'asana': 'Asana',
            'mondaycom': 'Monday.com',
            
            # AI/ML 服务
            'openai': 'OpenAI',
            'anthropic': 'Anthropic',
            'huggingface': 'Hugging Face',
            
            # 社交媒体
            'linkedin': 'LinkedIn',
            'twitter': 'Twitter/X',
            'facebook': 'Facebook',
            'instagram': 'Instagram',
            
            # 电子商务
            'shopify': 'Shopify',
            'stripe': 'Stripe',
            'paypal': 'PayPal',
            
            # 分析
            'googleanalytics': 'Google Analytics',
            'mixpanel': 'Mixpanel',
            
            # 日历与任务
            'googlecalendar': 'Google Calendar', 
            'googletasks': 'Google Tasks',
            'cal': 'Cal.com',
            'calendly': 'Calendly',
            
            # 表单与调查
            'typeform': 'Typeform',
            'googleforms': 'Google Forms',
            'form': 'Form Trigger',
            
            # 开发工具
            'webhook': 'Webhook',
            'httpRequest': 'HTTP Request',
            'graphql': 'GraphQL',
            'sse': 'Server-Sent Events',
            
            # 工具节点（从集成中排除）
            'set': None,
            'function': None,
            'code': None,
            'if': None,
            'switch': None,
            'merge': None,
            'split': None,
            'stickynote': None,
            'stickyNote': None,
            'wait': None,
            'schedule': None,
            'cron': None,
            'manual': None,
            'stopanderror': None,
            'noop': None,
            'noOp': None,
            'error': None,
            'limit': None,
            'aggregate': None,
            'summarize': None,
            'filter': None,
            'sort': None,
            'removeDuplicates': None,
            'dateTime': None,
            'extractFromFile': None,
            'convertToFile': None,
            'readBinaryFile': None,
            'readBinaryFiles': None,
            'executionData': None,
            'executeWorkflow': None,
            'executeCommand': None,
            'respondToWebhook': None,
        }
        
        for node in nodes:
            node_type = node.get('type', '')
            node_name = node.get('name', '').lower()
            
            # 确定触发器类型
            if 'webhook' in node_type.lower() or 'webhook' in node_name:
                trigger_type = 'Webhook'
            elif 'cron' in node_type.lower() or 'schedule' in node_type.lower():
                trigger_type = 'Scheduled'
            elif 'trigger' in node_type.lower() and trigger_type == 'Manual':
                if 'manual' not in node_type.lower():
                    trigger_type = 'Webhook'
            
            # 使用增强映射提取集成
            service_name = None
            
            # 处理 n8n-nodes-base 节点
            if node_type.startswith('n8n-nodes-base.'):
                raw_service = node_type.replace('n8n-nodes-base.', '').lower()
                raw_service = raw_service.replace('trigger', '')
                service_name = service_mappings.get(raw_service, raw_service.title() if raw_service else None)
            
            # 处理 @n8n/ 命名空间节点
            elif node_type.startswith('@n8n/'):
                raw_service = node_type.split('.')[-1].lower() if '.' in node_type else node_type.lower()
                raw_service = raw_service.replace('trigger', '')
                service_name = service_mappings.get(raw_service, raw_service.title() if raw_service else None)
            
            # 处理自定义节点
            elif '-' in node_type or '@' in node_type:
                # 尝试从自定义节点名称（如 "n8n-nodes-youtube-transcription-kasha.youtubeTranscripter"）中提取服务名称
                parts = node_type.lower().split('.')
                for part in parts:
                    if 'youtube' in part:
                        service_name = 'YouTube'
                        break
                    elif 'telegram' in part:
                        service_name = 'Telegram'
                        break
                    elif 'discord' in part:
                        service_name = 'Discord'
                        break
                    elif 'calcslive' in part:
                        service_name = 'CalcsLive'
                        break
            
            # 还检查节点名称以获取服务提示（但避免误报）
            for service_key, service_value in service_mappings.items():
                if service_key in node_name and service_value:
                    # 避免误报：calcslive相关术语中的 "cal" 不应匹配 "Cal.com"
                    if service_key == 'cal' and any(term in node_name.lower() for term in ['calcslive', 'calc', 'calculation']):
                        continue
                    service_name = service_value
                    break
            
            # 如果找到有效服务，则添加到集成列表
            if service_name and service_name not in ['None', None]:
                integrations.add(service_name)
        
        # 根据节点多样性和数量确定是否复杂
        if len(nodes) > 10 and len(integrations) > 3:
            trigger_type = 'Complex'
        
        return trigger_type, integrations
    
    def generate_description(self, workflow: Dict, trigger_type: str, integrations: set) -> str:
        """生成工作流的描述性摘要。"""
        name = workflow['name']
        node_count = workflow['node_count']
        
        # 以触发器描述开始
        trigger_descriptions = {
            'Webhook': "Webhook-triggered automation that",
            'Scheduled': "Scheduled automation that", 
            'Complex': "Complex multi-step automation that",
        }
        desc = trigger_descriptions.get(trigger_type, "Manual workflow that")
        
        # 根据名称和集成添加功能描述
        if integrations:
            main_services = list(integrations)[:3]
            if len(main_services) == 1:
                desc += f" integrates with {main_services[0]}"
            elif len(main_services) == 2:
                desc += f" connects {main_services[0]} and {main_services[1]}"
            else:
                desc += f" orchestrates {', '.join(main_services[:-1])}, and {main_services[-1]}"
        
        # 根据名称添加工作流用途提示
        name_lower = name.lower()
        if 'create' in name_lower:
            desc += " to create new records"
        elif 'update' in name_lower:
            desc += " to update existing data"
        elif 'sync' in name_lower:
            desc += " to synchronize data"
        elif 'notification' in name_lower or 'alert' in name_lower:
            desc += " for notifications and alerts"
        elif 'backup' in name_lower:
            desc += " for data backup operations"
        elif 'monitor' in name_lower:
            desc += " for monitoring and reporting"
        else:
            desc += " for data processing"
        
        desc += f". Uses {node_count} nodes"
        if len(integrations) > 3:
            desc += f" and integrates with {len(integrations)} services"
        
        return desc + "."
    
    def index_all_workflows(self, force_reindex: bool = False) -> Dict[str, int]:
        """索引所有工作流文件。除非设置 force_reindex=True，否则仅重新处理已更改的文件。"""
        if not os.path.exists(self.workflows_dir):
            print(f"警告: 工作流目录 '{self.workflows_dir}' 未找到。")
            return {'processed': 0, 'skipped': 0, 'errors': 0}
        
        workflows_path = Path(self.workflows_dir)
        json_files = [str(p) for p in workflows_path.rglob("*.json")]
        
        if not json_files:
            print(f"警告: 在 '{self.workflows_dir}' 目录中未找到 JSON 文件。")
            return {'processed': 0, 'skipped': 0, 'errors': 0}
        
        print(f"正在索引 {len(json_files)} 个工作流文件...")
        
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        stats = {'processed': 0, 'skipped': 0, 'errors': 0}
        
        for file_path in json_files:
            filename = os.path.basename(file_path)
            
            try:
                # 检查文件是否需要重新处理
                if not force_reindex:
                    current_hash = self.get_file_hash(file_path)
                    cursor = conn.execute(
                        "SELECT file_hash FROM workflows WHERE filename = ?", 
                        (filename,)
                    )
                    row = cursor.fetchone()
                    if row and row['file_hash'] == current_hash:
                        stats['skipped'] += 1
                        continue
                
                # 分析工作流
                workflow_data = self.analyze_workflow_file(file_path)
                if not workflow_data:
                    stats['errors'] += 1
                    continue
                
                # 在数据库中插入或更新
                conn.execute("""
                    INSERT OR REPLACE INTO workflows (
                        filename, name, workflow_id, active, description, trigger_type,
                        complexity, node_count, integrations, tags, created_at, updated_at,
                        file_hash, file_size, analyzed_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                """, (
                    workflow_data['filename'],
                    workflow_data['name'],
                    workflow_data['workflow_id'],
                    workflow_data['active'],
                    workflow_data['description'],
                    workflow_data['trigger_type'],
                    workflow_data['complexity'],
                    workflow_data['node_count'],
                    json.dumps(workflow_data['integrations']),
                    json.dumps(workflow_data['tags']),
                    workflow_data['created_at'],
                    workflow_data['updated_at'],
                    workflow_data['file_hash'],
                    workflow_data['file_size']
                ))
                
                stats['processed'] += 1
                
            except Exception as e:
                print(f"处理 {file_path} 时出错: {str(e)}")
                stats['errors'] += 1
                continue
        
        conn.commit()
        conn.close()
        
        print(f"✅ 索引完成: {stats['processed']} 已处理, {stats['skipped']} 已跳过, {stats['errors']} 个错误")
        return stats
    
    def search_workflows(self, query: str = "", trigger_filter: str = "all", 
                        complexity_filter: str = "all", active_only: bool = False,
                        limit: int = 50, offset: int = 0) -> Tuple[List[Dict], int]:
        """带筛选和分页的快速搜索。"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # 构建 WHERE 子句
        where_conditions = []
        params = []
        
        if active_only:
            where_conditions.append("w.active = 1")
        
        if trigger_filter != "all":
            where_conditions.append("w.trigger_type = ?")
            params.append(trigger_filter)
        
        if complexity_filter != "all":
            where_conditions.append("w.complexity = ?")
            params.append(complexity_filter)
        
        # 如果提供了查询，使用 FTS 搜索
        if query.strip():
            # 带排序的 FTS 搜索
            base_query = """
                SELECT w.*, rank
                FROM workflows_fts fts
                JOIN workflows w ON w.id = fts.rowid
                WHERE workflows_fts MATCH ?
            """
            params.insert(0, query)
        else:
            # 不使用 FTS 的常规查询
            base_query = """
                SELECT w.*, 0 as rank
                FROM workflows w
                WHERE 1=1
            """
        
        if where_conditions:
            base_query += " AND " + " AND ".join(where_conditions)
        
        # 统计总结果数
        count_query = f"SELECT COUNT(*) as total FROM ({base_query}) t"
        cursor = conn.execute(count_query, params)
        total = cursor.fetchone()['total']
        
        # 获取分页结果
        if query.strip():
            base_query += " ORDER BY rank"
        else:
            base_query += " ORDER BY w.analyzed_at DESC"
        
        base_query += f" LIMIT {limit} OFFSET {offset}"
        
        cursor = conn.execute(base_query, params)
        rows = cursor.fetchall()
        
        # 转换为字典并解析 JSON 字段
        results = []
        for row in rows:
            workflow = dict(row)
            workflow['integrations'] = json.loads(workflow['integrations'] or '[]')
            
            # 解析标签并将字典标签转换为字符串
            raw_tags = json.loads(workflow['tags'] or '[]')
            clean_tags = []
            for tag in raw_tags:
                if isinstance(tag, dict):
                    # 如果有标签字典，则提取名称
                    clean_tags.append(tag.get('name', str(tag.get('id', 'tag'))))
                else:
                    clean_tags.append(str(tag))
            workflow['tags'] = clean_tags
            
            results.append(workflow)
        
        conn.close()
        return results, total
    
    def get_stats(self) -> Dict[str, Any]:
        """获取数据库统计信息。"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # 基本统计
        cursor = conn.execute("SELECT COUNT(*) as total FROM workflows")
        total = cursor.fetchone()['total']
        
        cursor = conn.execute("SELECT COUNT(*) as active FROM workflows WHERE active = 1")
        active = cursor.fetchone()['active']
        
        # 触发器类型分类
        cursor = conn.execute("""
            SELECT trigger_type, COUNT(*) as count 
            FROM workflows 
            GROUP BY trigger_type
        """)
        triggers = {row['trigger_type']: row['count'] for row in cursor.fetchall()}
        
        # 复杂度分类
        cursor = conn.execute("""
            SELECT complexity, COUNT(*) as count 
            FROM workflows 
            GROUP BY complexity
        """)
        complexity = {row['complexity']: row['count'] for row in cursor.fetchall()}
        
        # 节点统计
        cursor = conn.execute("SELECT SUM(node_count) as total_nodes FROM workflows")
        total_nodes = cursor.fetchone()['total_nodes'] or 0
        
        # 唯一集成数量
        cursor = conn.execute("SELECT integrations FROM workflows WHERE integrations != '[]'")
        all_integrations = set()
        for row in cursor.fetchall():
            integrations = json.loads(row['integrations'])
            all_integrations.update(integrations)
        
        conn.close()
        
        return {
            'total': total,
            'active': active,
            'inactive': total - active,
            'triggers': triggers,
            'complexity': complexity,
            'total_nodes': total_nodes,
            'unique_integrations': len(all_integrations),
            'last_indexed': datetime.datetime.now().isoformat()
        }

    def get_service_categories(self) -> Dict[str, List[str]]:
        """获取服务类别以增强过滤功能。"""
        return {
            'messaging': ['Telegram', 'Discord', 'Slack', 'WhatsApp', 'Mattermost', 'Microsoft Teams', 'Rocket.Chat'],
            'email': ['Gmail', 'Mailjet', 'Email (IMAP)', 'Email (SMTP)', 'Outlook'],
            'cloud_storage': ['Google Drive', 'Google Docs', 'Google Sheets', 'Dropbox', 'OneDrive', 'Box'],
            'database': ['PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Airtable', 'Notion'],
            'project_management': ['Jira', 'GitHub', 'GitLab', 'Trello', 'Asana', 'Monday.com'],
            'ai_ml': ['OpenAI', 'Anthropic', 'Hugging Face', 'CalcsLive'],
            'social_media': ['LinkedIn', 'Twitter/X', 'Facebook', 'Instagram'],
            'ecommerce': ['Shopify', 'Stripe', 'PayPal'],
            'analytics': ['Google Analytics', 'Mixpanel'],
            'calendar_tasks': ['Google Calendar', 'Google Tasks', 'Cal.com', 'Calendly'],
            'forms': ['Typeform', 'Google Forms', 'Form Trigger'],
            'development': ['Webhook', 'HTTP Request', 'GraphQL', 'Server-Sent Events', 'YouTube']
        }

    def search_by_category(self, category: str, limit: int = 50, offset: int = 0) -> Tuple[List[Dict], int]:
        """按服务类别搜索工作流。"""
        categories = self.get_service_categories()
        if category not in categories:
            return [], 0
        
        services = categories[category]
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # 为类别中的所有服务构建OR条件
        service_conditions = []
        params = []
        for service in services:
            service_conditions.append("integrations LIKE ?")
            params.append(f'%"{service}"%')
        
        where_clause = " OR ".join(service_conditions)
        
        # 计算总结果数
        count_query = f"SELECT COUNT(*) as total FROM workflows WHERE {where_clause}"
        cursor = conn.execute(count_query, params)
        total = cursor.fetchone()['total']
        
        # 获取分页结果
        query = f"""
            SELECT * FROM workflows 
            WHERE {where_clause}
            ORDER BY analyzed_at DESC
            LIMIT {limit} OFFSET {offset}
        """
        
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()
        
        # 转换为字典并解析JSON字段
        results = []
        for row in rows:
            workflow = dict(row)
            workflow['integrations'] = json.loads(workflow['integrations'] or '[]')
            raw_tags = json.loads(workflow['tags'] or '[]')
            clean_tags = []
            for tag in raw_tags:
                if isinstance(tag, dict):
                    clean_tags.append(tag.get('name', str(tag.get('id', 'tag'))))
                else:
                    clean_tags.append(str(tag))
            workflow['tags'] = clean_tags
            results.append(workflow)
        
        conn.close()
        return results, total


def main():
    """工作流数据库的命令行界面。"""
    import argparse
    
    parser = argparse.ArgumentParser(description='N8N 工作流数据库')
    parser.add_argument('--index', action='store_true', help='索引所有工作流')
    parser.add_argument('--force', action='store_true', help='强制重新索引所有文件')
    parser.add_argument('--search', help='搜索工作流')
    parser.add_argument('--stats', action='store_true', help='显示数据库统计信息')
    
    args = parser.parse_args()
    
    db = WorkflowDatabase()
    
    if args.index:
        stats = db.index_all_workflows(force_reindex=args.force)
        print(f"已索引 {stats['processed']} 个工作流")
    
    elif args.search:
        results, total = db.search_workflows(args.search, limit=10)
        print(f"找到 {total} 个工作流:")
        for workflow in results:
            print(f"  - {workflow['name']} ({workflow['trigger_type']}, {workflow['node_count']} 个节点)")
    
    elif args.stats:
        stats = db.get_stats()
        print(f"数据库统计信息:")
        print(f"  总工作流数: {stats['total']}")
        print(f"  活跃工作流: {stats['active']}")
        print(f"  总节点数: {stats['total_nodes']}")
        print(f"  唯一集成数: {stats['unique_integrations']}")
        print(f"  触发器类型: {stats['triggers']}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
N8N 工作流文档的 FastAPI 服务器
高性能 API，响应时间低于 100ms。
"""

from fastapi import FastAPI, HTTPException, Query, BackgroundTasks, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict, Any
import json
import os
import asyncio
import re
import urllib.parse
from pathlib import Path
import uvicorn
import time
from collections import defaultdict

from workflow_db import WorkflowDatabase

# 初始化FastAPI应用
app = FastAPI(
    title="N8N 工作流文档 API",
    description="用于浏览和搜索工作流文档的快速API",
    version="2.0.0"
)

# 安全：速率限制存储
rate_limit_storage = defaultdict(list)
MAX_REQUESTS_PER_MINUTE = 60  # 根据需要配置

# 添加中间件以提高性能
app.add_middleware(GZipMiddleware, minimum_size=1000)

# 安全：正确配置CORS - 在生产环境中限制来源
# 对于本地开发，可以使用localhost
# 对于生产环境，请替换为您的实际域名
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "https://zie619.github.io",  # GitHub Pages
    "https://n8n-workflows-1-xxgm.onrender.com",  # Community deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # 安全修复：限制来源地址
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # 安全修复：仅允许需要的方法
    allow_headers=["Content-Type", "Authorization"],  # 安全修复：限制请求头
)

# 初始化数据库
db = WorkflowDatabase()

# 安全：速率限制辅助函数
def check_rate_limit(client_ip: str) -> bool:
    """检查客户端是否超出速率限制。"""
    current_time = time.time()
    # Clean old entries
    rate_limit_storage[client_ip] = [
        timestamp for timestamp in rate_limit_storage[client_ip]
        if current_time - timestamp < 60
    ]
    # Check rate limit
    if len(rate_limit_storage[client_ip]) >= MAX_REQUESTS_PER_MINUTE:
        return False
    # Add current request
    rate_limit_storage[client_ip].append(current_time)
    return True

# 安全：验证和清理文件名的辅助函数
def validate_filename(filename: str) -> bool:
    """
    验证文件名以防止路径遍历攻击。
    如果文件名安全返回True，否则返回False。
    """
    # 多次解码URL编码以捕获编码的遍历尝试
    decoded = filename
    for _ in range(3):  # 最多解码3次以捕获嵌套编码
        try:
            decoded = urllib.parse.unquote(decoded, errors='strict')
        except:
            return False  # 无效的编码

    # 检查路径遍历模式
    dangerous_patterns = [
        '..',  # 父目录
        '..\\',  # Windows父目录
        '../',  # Unix父目录
        '\\',  # 反斜杠 (Windows路径分隔符)
        '/',  # 正斜杠 (Unix路径分隔符)
        '\x00',  # 空字节
        '\n', '\r',  # 换行符
        '~',  # 主目录
        ':',  # 驱动器号或流 (Windows)
        '|', '<', '>',  # Shell重定向
        '*', '?',  # 通配符
        '$',  # 变量扩展
        ';', '&',  # 命令分隔符
    ]

    for pattern in dangerous_patterns:
        if pattern in decoded:
            return False

    # 检查绝对路径
    if decoded.startswith('/') or decoded.startswith('\\'):
        return False

    # 检查Windows驱动器号
    if len(decoded) >= 2 and decoded[1] == ':':
        return False

    # 仅允许字母数字、破折号、下划线和.json扩展名
    if not re.match(r'^[a-zA-Z0-9_\-]+\.json$', decoded):
        return False

    # 额外检查：文件名应以.json结尾
    if not decoded.endswith('.json'):
        return False

    return True

# 启动函数，用于验证数据库
@app.on_event("startup")
async def startup_event():
    """在启动时验证数据库连接。"""
    try:
        stats = db.get_stats()
        if stats['total'] == 0:
            print("⚠️  警告：数据库中未找到工作流。请先运行索引。")
        else:
            print(f"✅ 数据库已连接：已索引 {stats['total']} 个工作流")
    except Exception as e:
        print(f"❌ 数据库连接失败：{e}")
        raise

# 响应模型
class WorkflowSummary(BaseModel):
    id: Optional[int] = None
    filename: str
    name: str
    active: bool
    description: str = ""
    trigger_type: str = "Manual"
    complexity: str = "low"
    node_count: int = 0
    integrations: List[str] = []
    tags: List[str] = []
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        # 允许将整数转换为布尔值，用于active字段
        validate_assignment = True
        
    @field_validator('active', mode='before')
    @classmethod
    def convert_active(cls, v):
        if isinstance(v, int):
            return bool(v)
        return v
    

class SearchResponse(BaseModel):
    """
    搜索工作流的响应模型
    
    用于返回分页的工作流搜索结果和相关元数据
    """
    workflows: List[WorkflowSummary]  # 工作流列表，每个项包含工作流的详细信息
    total: int  # 匹配搜索条件的工作流总数
    page: int  # 当前页码
    per_page: int  # 每页显示的工作流数量
    pages: int  # 总页数
    query: str  # 搜索查询字符串
    filters: Dict[str, Any]  # 应用的过滤条件

class StatsResponse(BaseModel):
    """
    工作流统计信息的响应模型
    
    用于返回工作流数据库的统计信息和汇总数据
    """
    total: int  # 工作流总数
    active: int  # 活跃工作流数量
    inactive: int  # 非活跃工作流数量
    triggers: Dict[str, int]  # 按触发器类型分组的工作流计数
    complexity: Dict[str, int]  # 按复杂度分组的工作流计数
    total_nodes: int  # 所有工作流的节点总数
    unique_integrations: int  # 唯一集成的数量
    last_indexed: str  # 最后一次索引的时间戳

@app.get("/")
async def root():
    """提供主文档页面。"""
    static_dir = Path("static")
    index_file = static_dir / "index.html"
    if not index_file.exists():
        return HTMLResponse("""
        <html><body>
        <h1>需要设置</h1>
        <p>未找到静态文件。请确保静态目录存在且包含 index.html</p>
        <p>当前目录：""" + str(Path.cwd()) + """
        </body></html>
        """)
    return FileResponse(str(index_file))

@app.get("/health")
async def health_check():
    """健康检查端点。"""
    return {"status": "healthy", "message": "N8N 工作流 API 正在运行"}

@app.get("/api/stats", response_model=StatsResponse)
async def get_stats():
    """获取工作流数据库统计信息。"""
    try:
        stats = db.get_stats()
        return StatsResponse(**stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取统计信息失败: {str(e)}")

@app.get("/api/workflows", response_model=SearchResponse)
async def search_workflows(
    q: str = Query("", description="搜索查询"),
    trigger: str = Query("all", description="按触发器类型过滤"),
    complexity: str = Query("all", description="按复杂度过滤"),
    active_only: bool = Query(False, description="仅显示活跃工作流"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(20, ge=1, le=100, description="每页项数")
):
    """使用分页搜索和过滤工作流。"""
    try:
        offset = (page - 1) * per_page
        
        workflows, total = db.search_workflows(
            query=q,
            trigger_filter=trigger,
            complexity_filter=complexity,
            active_only=active_only,
            limit=per_page,
            offset=offset
        )
        
        # Convert to Pydantic models with error handling
        workflow_summaries = []
        for workflow in workflows:
            try:
                # Remove extra fields that aren't in the model
                clean_workflow = {
                    'id': workflow.get('id'),
                    'filename': workflow.get('filename', ''),
                    'name': workflow.get('name', ''),
                    'active': workflow.get('active', False),
                    'description': workflow.get('description', ''),
                    'trigger_type': workflow.get('trigger_type', 'Manual'),
                    'complexity': workflow.get('complexity', 'low'),
                    'node_count': workflow.get('node_count', 0),
                    'integrations': workflow.get('integrations', []),
                    'tags': workflow.get('tags', []),
                    'created_at': workflow.get('created_at'),
                    'updated_at': workflow.get('updated_at')
                }
                workflow_summaries.append(WorkflowSummary(**clean_workflow))
            except Exception as e:
                print(f"转换工作流 {workflow.get('filename', 'unknown')} 时出错：{e}")
                # Continue with other workflows instead of failing completely
                continue
        
        pages = (total + per_page - 1) // per_page  # Ceiling division
        
        return SearchResponse(
            workflows=workflow_summaries,
            total=total,
            page=page,
            per_page=per_page,
            pages=pages,
            query=q,
            filters={
                "trigger": trigger,
                "complexity": complexity,
                "active_only": active_only
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"搜索工作流失败: {str(e)}")

@app.get("/api/workflows/{filename}")
async def get_workflow_detail(filename: str, request: Request):
    """获取工作流详细信息，包括原始JSON。"""
    try:
        # 安全：验证文件名以防止路径遍历
        if not validate_filename(filename):
            print(f"安全：已阻止对文件名的路径遍历尝试：{filename}")
            raise HTTPException(status_code=400, detail="无效的文件名格式")

        # 安全：速率限制
        client_ip = request.client.host if request.client else "unknown"
        if not check_rate_limit(client_ip):
            raise HTTPException(status_code=429, detail="请求频率过高，请稍后再试。")

        # 从数据库获取工作流元数据
        workflows, _ = db.search_workflows(f'filename:"{filename}"', limit=1)
        if not workflows:
            raise HTTPException(status_code=404, detail="数据库中未找到工作流")

        workflow_meta = workflows[0]

        # 从文件加载原始JSON（包含安全检查）
        workflows_path = Path('workflows').resolve()

        # 安全地查找文件
        matching_file = None
        for subdir in workflows_path.iterdir():
            if subdir.is_dir():
                target_file = subdir / filename
                if target_file.exists() and target_file.is_file():
                    # 验证文件确实在工作流目录内
                    try:
                        target_file.resolve().relative_to(workflows_path)
                        matching_file = target_file
                        break
                    except ValueError:
                        print(f"安全：已阻止访问工作流目录外的文件：{target_file}")
                        continue

        if not matching_file:
            print(f"警告：在工作流目录中未找到文件 {filename}")
            raise HTTPException(status_code=404, detail=f"文件系统中未找到工作流文件 '{filename}'")

        with open(matching_file, 'r', encoding='utf-8') as f:
            raw_json = json.load(f)

        return {
            "metadata": workflow_meta,
            "raw_json": raw_json
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"加载工作流失败: {str(e)}")

@app.get("/api/workflows/{filename}/download")
async def download_workflow(filename: str, request: Request):
    """下载工作流JSON文件（包含安全验证）。"""
    try:
        # Security: Validate filename to prevent path traversal
        if not validate_filename(filename):
            print(f"安全：已阻止对文件名的路径遍历尝试：{filename}")
            raise HTTPException(status_code=400, detail="无效的文件名格式")

        # Security: Rate limiting
        client_ip = request.client.host if request.client else "unknown"
        if not check_rate_limit(client_ip):
            raise HTTPException(status_code=429, detail="请求频率过高，请稍后再试。")

        # 仅在工作流目录内搜索
        workflows_path = Path('workflows').resolve()  # Get absolute path

        # Find the file safely
        json_files = []
        for subdir in workflows_path.iterdir():
            if subdir.is_dir():
                target_file = subdir / filename
                if target_file.exists() and target_file.is_file():
                    # 验证文件确实在工作流目录内（纵深防御）
                    try:
                        target_file.resolve().relative_to(workflows_path)
                        json_files.append(target_file)
                    except ValueError:
                        # 文件在工作流目录外
                        print(f"安全：已阻止访问工作流目录外的文件：{target_file}")
                        continue

        if not json_files:
            print(f"在工作流目录中未找到文件 {filename}")
            raise HTTPException(status_code=404, detail=f"未找到工作流文件 '{filename}'")

        file_path = json_files[0]

        # 最终安全检查：确保文件在工作流目录内
        try:
            file_path.resolve().relative_to(workflows_path)
        except ValueError:
            print(f"安全：已阻止最终访问工作流目录外文件的尝试：{file_path}")
            raise HTTPException(status_code=403, detail="访问被拒绝")

        return FileResponse(
            str(file_path),
            media_type="application/json",
            filename=filename
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"下载工作流 {filename} 时出错：{str(e)}")
        raise HTTPException(status_code=500, detail=f"下载工作流失败: {str(e)}")

@app.get("/api/workflows/{filename}/diagram")
async def get_workflow_diagram(filename: str, request: Request):
    """获取用于工作流可视化的Mermaid图表代码。"""
    try:
        # Security: Validate filename to prevent path traversal
        if not validate_filename(filename):
            print(f"安全：已阻止对文件名的路径遍历尝试：{filename}")
            raise HTTPException(status_code=400, detail="无效的文件名格式")

        # Security: Rate limiting
        client_ip = request.client.host if request.client else "unknown"
        if not check_rate_limit(client_ip):
            raise HTTPException(status_code=429, detail="请求频率过高，请稍后再试。")

        # Only search within the workflows directory
        workflows_path = Path('workflows').resolve()

        # Find the file safely
        matching_file = None
        for subdir in workflows_path.iterdir():
            if subdir.is_dir():
                target_file = subdir / filename
                if target_file.exists() and target_file.is_file():
                    # Verify the file is actually within workflows directory
                    try:
                        target_file.resolve().relative_to(workflows_path)
                        matching_file = target_file
                        break
                    except ValueError:
                        print(f"安全：已阻止访问工作流目录外的文件：{target_file}")
                        continue

        if not matching_file:
            print(f"警告：在工作流目录中未找到文件 {filename}")
            raise HTTPException(status_code=404, detail=f"Workflow file '{filename}' not found on filesystem")

        with open(matching_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        nodes = data.get('nodes', [])
        connections = data.get('connections', {})

        # 生成Mermaid图表
        diagram = generate_mermaid_diagram(nodes, connections)

        return {"diagram": diagram}
    except HTTPException:
        raise
    except json.JSONDecodeError as e:
        print(f"解析 {filename} 中的JSON时出错：{str(e)}")
        raise HTTPException(status_code=400, detail=f"工作流文件中的JSON无效: {str(e)}")
    except Exception as e:
        print(f"为 {filename} 生成图表时出错：{str(e)}")
        raise HTTPException(status_code=500, detail=f"生成图表失败: {str(e)}")

def generate_mermaid_diagram(nodes: List[Dict], connections: Dict) -> str:
    """从工作流节点和连接生成Mermaid.js流程图代码。"""
    if not nodes:
        return "graph TD\n  EmptyWorkflow[No nodes found in workflow]"
    
    # 创建节点名称映射以确保有效的mermaid ID
    mermaid_ids = {}
    for i, node in enumerate(nodes):
        node_id = f"node{i}"
        node_name = node.get('name', f'Node {i}')
        mermaid_ids[node_name] = node_id
    
    # 开始构建mermaid图表
    mermaid_code = ["graph TD"]
    
    # 添加带样式的节点
    for node in nodes:
        node_name = node.get('name', 'Unnamed')
        node_id = mermaid_ids[node_name]
        node_type = node.get('type', '').replace('n8n-nodes-base.', '')
        
        # 根据类型确定节点样式
        style = ""
        if any(x in node_type.lower() for x in ['trigger', 'webhook', 'cron']):
            style = "fill:#b3e0ff,stroke:#0066cc"  # Blue for triggers
        elif any(x in node_type.lower() for x in ['if', 'switch']):
            style = "fill:#ffffb3,stroke:#e6e600"  # Yellow for conditional nodes
        elif any(x in node_type.lower() for x in ['function', 'code']):
            style = "fill:#d9b3ff,stroke:#6600cc"  # Purple for code nodes
        elif 'error' in node_type.lower():
            style = "fill:#ffb3b3,stroke:#cc0000"  # Red for error handlers
        else:
            style = "fill:#d9d9d9,stroke:#666666"  # Gray for other nodes
        
        # Add node with label (escaping special characters)
        clean_name = node_name.replace('"', "'")
        clean_type = node_type.replace('"', "'")
        label = f"{clean_name}<br>({clean_type})"
        mermaid_code.append(f"  {node_id}[\"{label}\"]")
        mermaid_code.append(f"  style {node_id} {style}")
    
    # 添加节点之间的连接
    for source_name, source_connections in connections.items():
        if source_name not in mermaid_ids:
            continue
        
        if isinstance(source_connections, dict) and 'main' in source_connections:
            main_connections = source_connections['main']
            
            for i, output_connections in enumerate(main_connections):
                if not isinstance(output_connections, list):
                    continue
                    
                for connection in output_connections:
                    if not isinstance(connection, dict) or 'node' not in connection:
                        continue
                        
                    target_name = connection['node']
                    if target_name not in mermaid_ids:
                        continue
                        
                    # Add arrow with output index if multiple outputs
                    label = f" -->|{i}| " if len(main_connections) > 1 else " --> "
                    mermaid_code.append(f"  {mermaid_ids[source_name]}{label}{mermaid_ids[target_name]}")
    
    # Format the final mermaid diagram code
    return "\n".join(mermaid_code)

@app.post("/api/reindex")
async def reindex_workflows(
    background_tasks: BackgroundTasks,
    request: Request,
    force: bool = False,
    admin_token: Optional[str] = Query(None, description="管理员认证令牌")
):
    """在后台触发工作流重新索引（需要认证）。"""
    # Security: Rate limiting
    client_ip = request.client.host if request.client else "unknown"
    if not check_rate_limit(client_ip):
        raise HTTPException(status_code=429, detail="请求频率过高，请稍后再试。")

    # 安全：基本认证检查
    # 在生产环境中，使用适当的认证（JWT、OAuth等）
# 目前，检查环境变量或禁用端点
    import os
    expected_token = os.environ.get("ADMIN_TOKEN", None)

    if not expected_token:
        # 如果未配置令牌，则为安全起见禁用该端点
        raise HTTPException(
            status_code=503,
            detail="重新索引端点已禁用。设置 ADMIN_TOKEN 环境变量以启用。"
        )

    if admin_token != expected_token:
        print(f"安全：来自 {client_ip} 的未授权重新索引尝试")
        raise HTTPException(status_code=401, detail="无效的认证令牌")

    def run_indexing():
        try:
            db.index_all_workflows(force_reindex=force)
            print(f"重新索引成功完成（由 {client_ip} 请求）")
        except Exception as e:
            print(f"重新索引期间出错：{e}")

    background_tasks.add_task(run_indexing)
    return {"message": "后台重新索引已开始", "requested_by": client_ip}

@app.get("/api/integrations")
async def get_integrations():
    """获取所有唯一集成的列表。"""
    try:
        stats = db.get_stats()
        # 目前，返回基本信息。可以增强以返回详细的集成统计信息
        return {"integrations": [], "count": stats['unique_integrations']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取集成失败: {str(e)}")

@app.get("/api/categories")
async def get_categories():
    """获取用于过滤的可用工作流类别。"""
    try:
        # 尝试从生成的唯一类别文件加载
        categories_file = Path("context/unique_categories.json")
        if categories_file.exists():
            with open(categories_file, 'r', encoding='utf-8') as f:
                categories = json.load(f)
            return {"categories": categories}
        else:
            # 备选方案：从search_categories.json提取类别
            search_categories_file = Path("context/search_categories.json")
            if search_categories_file.exists():
                with open(search_categories_file, 'r', encoding='utf-8') as f:
                    search_data = json.load(f)
                
                unique_categories = set()
                for item in search_data:
                    if item.get('category'):
                        unique_categories.add(item['category'])
                    else:
                        unique_categories.add('未分类')
                
                categories = sorted(list(unique_categories))
                return {"categories": categories}
            else:
                # 最后手段：返回基本类别
                return {"categories": ["未分类"]}
                
    except Exception as e:
        print(f"加载类别时出错：{e}")
        raise HTTPException(status_code=500, detail=f"获取类别失败: {str(e)}")

@app.get("/api/category-mappings")
async def get_category_mappings():
    """获取文件名到类别的映射，用于客户端过滤。"""
    try:
        search_categories_file = Path("context/search_categories.json")
        if not search_categories_file.exists():
            return {"mappings": {}}
        
        with open(search_categories_file, 'r', encoding='utf-8') as f:
            search_data = json.load(f)
        
        # 转换为简单的文件名 -> 类别映射
        mappings = {}
        for item in search_data:
            filename = item.get('filename')
            category = item.get('category') or '未分类'
            if filename:
                mappings[filename] = category
        
        return {"mappings": mappings}
        
    except Exception as e:
        print(f"加载类别映射时出错：{e}")
        raise HTTPException(status_code=500, detail=f"获取类别映射失败: {str(e)}")

@app.get("/api/workflows/category/{category}", response_model=SearchResponse)
async def search_workflows_by_category(
    category: str,
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(20, ge=1, le=100, description="每页项数")
):
    """按服务类别（消息传递、数据库、ai_ml等）搜索工作流。"""
    try:
        offset = (page - 1) * per_page
        
        workflows, total = db.search_by_category(
            category=category,
            limit=per_page,
            offset=offset
        )
        
        # Convert to Pydantic models with error handling
        workflow_summaries = []
        for workflow in workflows:
            try:
                clean_workflow = {
                    'id': workflow.get('id'),
                    'filename': workflow.get('filename', ''),
                    'name': workflow.get('name', ''),
                    'active': workflow.get('active', False),
                    'description': workflow.get('description', ''),
                    'trigger_type': workflow.get('trigger_type', 'Manual'),
                    'complexity': workflow.get('complexity', 'low'),
                    'node_count': workflow.get('node_count', 0),
                    'integrations': workflow.get('integrations', []),
                    'tags': workflow.get('tags', []),
                    'created_at': workflow.get('created_at'),
                    'updated_at': workflow.get('updated_at')
                }
                workflow_summaries.append(WorkflowSummary(**clean_workflow))
            except Exception as e:
                print(f"转换工作流 {workflow.get('filename', 'unknown')} 时出错：{e}")
                continue
        
        pages = (total + per_page - 1) // per_page
        
        return SearchResponse(
            workflows=workflow_summaries,
            total=total,
            page=page,
            per_page=per_page,
            pages=pages,
            query=f"category:{category}",
            filters={"category": category}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"按类别搜索失败: {str(e)}")

# 自定义异常处理器，提供更好的错误响应
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": f"内部服务器错误: {str(exc)}"}
    )

# 在定义所有路由后挂载静态文件
static_dir = Path("static")
if static_dir.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    print(f"✅ 静态文件已从 {static_dir.absolute()} 挂载")
else:
    print(f"❌ 警告：在 {static_dir.absolute()} 未找到静态目录")

def create_static_directory():
    """如果静态目录不存在，则创建它。"""
    static_dir = Path("static")
    static_dir.mkdir(exist_ok=True)
    return static_dir

def run_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """运行FastAPI服务器。"""
    # 确保静态目录存在
    create_static_directory()
    
    # 调试：检查数据库连接
    try:
        stats = db.get_stats()
        print(f"✅ 数据库已连接：找到 {stats['total']} 个工作流")
        if stats['total'] == 0:
            print("🔄 数据库为空。正在索引工作流...")
            db.index_all_workflows()
            stats = db.get_stats()
    except Exception as e:
        print(f"❌ 数据库错误：{e}")
        print("🔄 正在尝试创建和索引数据库...")
        try:
            db.index_all_workflows()
            stats = db.get_stats()
            print(f"✅ 数据库已创建：已索引 {stats['total']} 个工作流")
        except Exception as e2:
            print(f"❌ 创建数据库失败：{e2}")
            stats = {'total': 0}
    
    # 调试：检查静态文件
    static_path = Path("static")
    if static_path.exists():
        files = list(static_path.glob("*"))
        print(f"✅ 找到静态文件：{[f.name for f in files]}")
    else:
        print(f"❌ 在 {static_path.absolute()} 未找到静态目录")
    
    print(f"🚀 正在启动 N8N 工作流文档 API")
    print(f"📊 数据库包含 {stats['total']} 个工作流")
    print(f"🌐 服务器将在以下地址可用：http://{host}:{port}")
    print(f"📁 静态文件位置：http://{host}:{port}/static/")
    
    uvicorn.run(
        "api_server:app",
        host=host,
        port=port,
        reload=reload,
        access_log=True,  # Enable access logs for debugging
        log_level="info"
    )

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='N8N 工作流文档 API 服务器')
    parser.add_argument('--host', default='127.0.0.1', help='绑定的主机地址')
    parser.add_argument('--port', type=int, default=8000, help='绑定的端口号')
    parser.add_argument('--reload', action='store_true', help='为开发环境启用自动重载功能')
    
    args = parser.parse_args()
    
    run_server(host=args.host, port=args.port, reload=args.reload)
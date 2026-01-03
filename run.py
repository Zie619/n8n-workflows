#!/usr/bin/env python3
"""
🚀 N8N工作流搜索引擎启动器
启动性能优化的高级搜索系统。
"""

import sys
import os
import argparse
from pathlib import Path


def print_banner():
    """打印应用程序横幅。"""
    print("🚀 n8n-workflows高级搜索引擎")
    print("=" * 50)


def check_requirements() -> bool:
    """检查是否安装了所需的依赖项。"""
    missing_deps = []
    
    try:
        import sqlite3
    except ImportError:
        missing_deps.append("sqlite3")
    
    try:
        import uvicorn
    except ImportError:
        missing_deps.append("uvicorn")
    
    try:
        import fastapi
    except ImportError:
        missing_deps.append("fastapi")
    
    if missing_deps:
        print(f"❌ 缺少依赖项: {', '.join(missing_deps)}")
        print("💡 安装命令: pip install -r requirements.txt")
        return False
    
    print("✅ 依赖项已验证")
    return True


def setup_directories():
    """创建必要的目录。"""
    directories = ["database", "static", "workflows"]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("✅ 目录已验证")


def setup_database(force_reindex: bool = False, skip_index: bool = False) -> str:
    """设置并初始化数据库。"""
    from workflow_db import WorkflowDatabase

    db_path = "database/workflows.db"

    print(f"🔄 设置数据库: {db_path}")
    db = WorkflowDatabase(db_path)

    # 在CI模式或明确请求时跳过索引
    if skip_index:
        print("⏭️  跳过工作流索引 (CI模式)")
        stats = db.get_stats()
        print(f"✅ 数据库已准备就绪: {stats['total']} 个工作流")
        return db_path

    # 检查数据库是否有数据或强制重建索引
    stats = db.get_stats()
    if stats['total'] == 0 or force_reindex:
        print("📚 正在为工作流建立索引...")
        index_stats = db.index_all_workflows(force_reindex=True)
        print(f"✅ 已索引 {index_stats['processed']} 个工作流")

        # 显示最终统计信息
        final_stats = db.get_stats()
        print(f"📊 数据库包含 {final_stats['total']} 个工作流")
    else:
        print(f"✅ 数据库已准备就绪: {stats['total']} 个工作流")

    return db_path


def start_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """启动FastAPI服务器。"""
    print(f"🌐 服务器正在启动: http://{host}:{port}")
    print(f"📊 API文档: http://{host}:{port}/docs")
    print(f"🔍 工作流搜索: http://{host}:{port}/api/workflows")
    print()
    print("按Ctrl+C停止服务器")
    print("-" * 50)
    
    # 配置数据库路径
    os.environ['WORKFLOW_DB_PATH'] = "database/workflows.db"
    
    # 使用优化配置启动uvicorn
    import uvicorn
    uvicorn.run(
        "api_server:app", 
        host=host, 
        port=port, 
        reload=reload,
        log_level="info",
        access_log=False  # Reduce log noise
    )


def main():
    """带命令行参数的主入口点。"""
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(
        description="N8N工作流搜索引擎",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python run.py                    # 使用默认设置启动
  python run.py --port 3000        # 在端口3000上启动
  python run.py --host 0.0.0.0     # 接受外部连接
  python run.py --reindex          # 强制数据库重建索引
  python run.py --dev              # 开发模式，带自动重载
        """
    )
    
    parser.add_argument(
        "--host", 
        default="127.0.0.1", 
        help="要绑定的主机 (默认: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="要绑定的端口 (默认: 8000)"
    )
    parser.add_argument(
        "--reindex", 
        action="store_true", 
        help="强制数据库重建索引"
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="开发模式，带自动重载"
    )
    parser.add_argument(
        "--skip-index",
        action="store_true",
        help="跳过工作流索引 (对CI/测试有用)"
    )

    args = parser.parse_args()

    # 同时检查CI模式的环境变量
    ci_mode = os.environ.get('CI', '').lower() in ('true', '1', 'yes')
    skip_index = args.skip_index or ci_mode
    
    print_banner()
    
    # 检查依赖项
    if not check_requirements():
        sys.exit(1)
    
    # 设置目录
    setup_directories()
    
    # 设置数据库
    try:
        setup_database(force_reindex=args.reindex, skip_index=skip_index)
    except Exception as e:
        print(f"❌ 数据库设置错误: {e}")
        sys.exit(1)
    
    # 启动服务器
    try:
        start_server(
            host=args.host, 
            port=args.port, 
            reload=args.dev
        )
    except KeyboardInterrupt:
        print("\n👋 服务器已停止!")
    except Exception as e:
        print(f"❌ 服务器错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
为 GitHub Pages 生成静态搜索索引
创建用于客户端搜索功能的轻量级 JSON 索引。
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

# 将父目录添加到导入路径
sys.path.append(str(Path(__file__).parent.parent))

from workflow_db import WorkflowDatabase


def generate_static_search_index(db_path: str, output_dir: str) -> Dict[str, Any]:
    """为客户端搜索生成静态搜索索引。"""

    # 初始化数据库
    db = WorkflowDatabase(db_path)

    # 获取所有工作流
    workflows, total = db.search_workflows(limit=10000)  # Get all workflows

    # 获取统计信息
    stats = db.get_stats()

    # 从服务映射中获取分类
    categories = db.get_service_categories()

    # 从 create_categories.py 系统加载现有分类
    existing_categories = load_existing_categories()

    # 创建简化的工作流搜索数据
    search_workflows = []
    for workflow in workflows:
        # 组合多个字段创建可搜索文本
        searchable_text = ' '.join([
            workflow['name'],
            workflow['description'],
            workflow['filename'],
            ' '.join(workflow['integrations']),
            ' '.join(workflow['tags']) if workflow['tags'] else ''
        ]).lower()

        # 使用 create_categories.py 系统中的现有分类，如果没有则使用基于集成的分类
        category = get_workflow_category(workflow['filename'], existing_categories, workflow['integrations'], categories)

        search_workflow = {
            'id': workflow['filename'].replace('.json', ''),
            'name': workflow['name'],
            'description': workflow['description'],
            'filename': workflow['filename'],
            'active': workflow['active'],
            'trigger_type': workflow['trigger_type'],
            'complexity': workflow['complexity'],
            'node_count': workflow['node_count'],
            'integrations': workflow['integrations'],
            'tags': workflow['tags'],
            'category': category,
            'searchable_text': searchable_text,
            'download_url': f"https://raw.githubusercontent.com/Zie619/n8n-workflows/main/workflows/{extract_folder_from_filename(workflow['filename'])}/{workflow['filename']}"
        }
        search_workflows.append(search_workflow)

    # Create comprehensive search index
    search_index = {
        'version': '1.0',
        'generated_at': stats.get('last_indexed', ''),
        'stats': {
            'total_workflows': stats['total'],
            'active_workflows': stats['active'],
            'inactive_workflows': stats['inactive'],
            'total_nodes': stats['total_nodes'],
            'unique_integrations': stats['unique_integrations'],
            'categories': len(get_category_list(categories)),
            'triggers': stats['triggers'],
            'complexity': stats['complexity']
        },
        'categories': get_category_list(categories),
        'integrations': get_popular_integrations(workflows),
        'workflows': search_workflows
    }

    return search_index


def load_existing_categories() -> Dict[str, str]:
    """从 create_categories.py 创建的 search_categories.json 加载现有分类。"""
    try:
        with open('context/search_categories.json', 'r', encoding='utf-8') as f:
            categories_data = json.load(f)

        # 转换为文件名 -> 分类映射
        category_mapping = {}
        for item in categories_data:
            if item.get('category'):
                category_mapping[item['filename']] = item['category']

        return category_mapping
    except FileNotFoundError:
        print("警告：未找到 search_categories.json，使用基于集成的分类")
        return {}


def get_workflow_category(filename: str, existing_categories: Dict[str, str],
                         integrations: List[str], service_categories: Dict[str, List[str]]) -> str:
    """获取工作流的分类，优先使用现有分配而非基于集成的分类。"""

    # 第一优先级：使用 create_categories.py 系统中的现有分类
    if filename in existing_categories:
        return existing_categories[filename]

    # 回退方案：使用基于集成的分类
    return determine_category(integrations, service_categories)


def determine_category(integrations: List[str], categories: Dict[str, List[str]]) -> str:
    """根据工作流的集成来确定其分类。"""
    if not integrations:
        return "未分类"

    # 检查每个分类是否有匹配的集成
    for category, services in categories.items():
        for integration in integrations:
            if integration in services:
                return format_category_name(category)

    return "未分类"


def format_category_name(category_key: str) -> str:
    """将分类键格式化为显示名称。"""
    category_mapping = {
        'messaging': '通信与消息',
        'email': '通信与消息',
        'cloud_storage': '云存储与文件管理',
        'database': '数据处理与分析',
        'project_management': '项目管理',
        'ai_ml': 'AI 代理开发',
        'social_media': '社交媒体管理',
        'ecommerce': '电子商务与零售',
        'analytics': '数据处理与分析',
        'calendar_tasks': '项目管理',
        'forms': '数据处理与分析',
        'development': '技术基础设施与开发运维'
    }
    return category_mapping.get(category_key, category_key.replace('_', ' ').title())


def get_category_list(categories: Dict[str, List[str]]) -> List[str]:
    """获取所有分类的格式化列表。"""
    formatted_categories = set()
    for category_key in categories.keys():
        formatted_categories.add(format_category_name(category_key))

    # 添加 create_categories.py 系统中的分类
    additional_categories = [
        "业务流程自动化",
        "网页抓取与数据提取",
        "营销与广告自动化",
        "创意内容与视频自动化",
        "创意设计自动化",
        "客户关系管理与销售",
        "财务与会计"
    ]

    for cat in additional_categories:
        formatted_categories.add(cat)

    return sorted(list(formatted_categories))


def get_popular_integrations(workflows: List[Dict]) -> List[Dict[str, Any]]:
    """获取带计数的热门集成列表。"""
    integration_counts = {}

    for workflow in workflows:
        for integration in workflow['integrations']:
            integration_counts[integration] = integration_counts.get(integration, 0) + 1

    # Sort by count and take top 50
    sorted_integrations = sorted(
        integration_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:50]

    return [
        {'name': name, 'count': count}
        for name, count in sorted_integrations
    ]


def extract_folder_from_filename(filename: str) -> str:
    """从工作流文件名中提取文件夹名称。"""
    # 大多数工作流遵循模式：ID_Service_Purpose_Trigger.json
    # 提取服务名称作为文件夹
    parts = filename.replace('.json', '').split('_')
    if len(parts) >= 2:
        return parts[1].capitalize()  # Second part is usually the service
    return 'Misc'


def save_search_index(search_index: Dict[str, Any], output_dir: str):
    """将搜索索引保存为多种格式以用于不同用途。"""

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 保存完整索引
    with open(os.path.join(output_dir, 'search-index.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)

    # 仅保存统计信息（用于快速加载）
    with open(os.path.join(output_dir, 'stats.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index['stats'], f, indent=2, ensure_ascii=False)

    # 仅保存分类
    with open(os.path.join(output_dir, 'categories.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index['categories'], f, indent=2, ensure_ascii=False)

    # 仅保存集成
    with open(os.path.join(output_dir, 'integrations.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index['integrations'], f, indent=2, ensure_ascii=False)

    print(f"搜索索引生成成功：")
    print(f"   {search_index['stats']['total_workflows']} 个工作流已索引")
    print(f"   {len(search_index['categories'])} 个分类")
    print(f"   {len(search_index['integrations'])} 个热门集成")
    print(f"   文件已保存至：{output_dir}")


def main():
    """生成搜索索引的主函数。"""

    # 路径
    db_path = "database/workflows.db"
    output_dir = "docs/api"

    # 检查数据库是否存在
    if not os.path.exists(db_path):
        print(f"未找到数据库：{db_path}")
        print("请先运行 'python run.py --reindex' 创建数据库")
        sys.exit(1)

    try:
        print("正在生成静态搜索索引...")
        search_index = generate_static_search_index(db_path, output_dir)
        save_search_index(search_index, output_dir)

        print("GitHub Pages 的静态搜索索引已准备就绪！")

    except Exception as e:
        print(f"生成搜索索引时出错：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
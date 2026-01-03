#!/usr/bin/env python3
"""
使用当前工作流统计信息更新 README.md
将硬编码的数字替换为数据库中的实时数据。
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Add the parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from workflow_db import WorkflowDatabase


def get_current_stats():
    """从数据库获取当前工作流统计信息。"""
    db_path = "database/workflows.db"

    if not os.path.exists(db_path):
        print("未找到数据库。请先运行工作流索引。")
        return None

    db = WorkflowDatabase(db_path)
    stats = db.get_stats()

    # 获取类别计数
    categories = db.get_service_categories()

    return {
        'total_workflows': stats['total'],
        'active_workflows': stats['active'],
        'inactive_workflows': stats['inactive'],
        'total_nodes': stats['total_nodes'],
        'unique_integrations': stats['unique_integrations'],
        'categories_count': len(get_category_list(categories)),
        'triggers': stats['triggers'],
        'complexity': stats['complexity'],
        'last_updated': datetime.now().strftime('%Y-%m-%d')
    }


def get_category_list(categories):
    """获取所有类别的格式化列表（与搜索索引相同的逻辑）。"""
    formatted_categories = set()

    # 将技术类别映射到显示名称
    category_mapping = {
        'messaging': 'Communication & Messaging',
        'email': 'Communication & Messaging',
        'cloud_storage': 'Cloud Storage & File Management',
        'database': 'Data Processing & Analysis',
        'project_management': 'Project Management',
        'ai_ml': 'AI Agent Development',
        'social_media': 'Social Media Management',
        'ecommerce': 'E-commerce & Retail',
        'analytics': 'Data Processing & Analysis',
        'calendar_tasks': 'Project Management',
        'forms': 'Data Processing & Analysis',
        'development': 'Technical Infrastructure & DevOps'
    }

    for category_key in categories.keys():
        display_name = category_mapping.get(category_key, category_key.replace('_', ' ').title())
        formatted_categories.add(display_name)

    # 添加来自 create_categories.py 系统的类别
    additional_categories = [
        "Business Process Automation",
        "Web Scraping & Data Extraction",
        "Marketing & Advertising Automation",
        "Creative Content & Video Automation",
        "Creative Design Automation",
        "CRM & Sales",
        "Financial & Accounting"
    ]

    for cat in additional_categories:
        formatted_categories.add(cat)

    return sorted(list(formatted_categories))


def update_readme_stats(stats):
    """使用当前统计信息更新 README.md。"""
    readme_path = "README.md"

    if not os.path.exists(readme_path):
        print("未找到 README.md")
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacement patterns and their new values
    replacements = [
        # Main collection description
        (r'A professionally organized collection of \*\*[\d,]+\s+n8n workflows\*\*',
         f'A professionally organized collection of **{stats["total_workflows"]:,} n8n workflows**'),

        # Total workflows in various contexts
        (r'- \*\*[\d,]+\s+workflows\*\* with meaningful',
         f'- **{stats["total_workflows"]:,} workflows** with meaningful'),

        # Statistics section
        (r'- \*\*Total Workflows\*\*: [\d,]+',
         f'- **Total Workflows**: {stats["total_workflows"]:,}'),

        (r'- \*\*Active Workflows\*\*: [\d,]+ \([\d.]+%',
         f'- **Active Workflows**: {stats["active_workflows"]:,} ({(stats["active_workflows"]/stats["total_workflows"]*100):.1f}%'),

        (r'- \*\*Total Nodes\*\*: [\d,]+ \(avg [\d.]+ nodes',
         f'- **Total Nodes**: {stats["total_nodes"]:,} (avg {(stats["total_nodes"]/stats["total_workflows"]):.1f} nodes'),

        (r'- \*\*Unique Integrations\*\*: [\d,]+ different',
         f'- **Unique Integrations**: {stats["unique_integrations"]:,} different'),

        # 更新复杂度/触发器分布
        (r'- \*\*Complex\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Complex**: {stats["triggers"].get("Complex", 0):,} workflows ({(stats["triggers"].get("Complex", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Webhook\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Webhook**: {stats["triggers"].get("Webhook", 0):,} workflows ({(stats["triggers"].get("Webhook", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Manual\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Manual**: {stats["triggers"].get("Manual", 0):,} workflows ({(stats["triggers"].get("Manual", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Scheduled\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Scheduled**: {stats["triggers"].get("Scheduled", 0):,} workflows ({(stats["triggers"].get("Scheduled", 0)/stats["total_workflows"]*100):.1f}%)'),

        # 更新当前集合统计信息中的总数
        (r'\*\*Total Workflows\*\*: [\d,]+ automation',
         f'**Total Workflows**: {stats["total_workflows"]:,} automation'),

        (r'\*\*Active Workflows\*\*: [\d,]+ \([\d.]+% active',
         f'**Active Workflows**: {stats["active_workflows"]:,} ({(stats["active_workflows"]/stats["total_workflows"]*100):.1f}% active'),

        (r'\*\*Total Nodes\*\*: [\d,]+ \(avg [\d.]+ nodes',
         f'**Total Nodes**: {stats["total_nodes"]:,} (avg {(stats["total_nodes"]/stats["total_workflows"]):.1f} nodes'),

        (r'\*\*Unique Integrations\*\*: [\d,]+ different',
         f'**Unique Integrations**: {stats["unique_integrations"]:,} different'),

        # 类别计数
        (r'Our system automatically categorizes workflows into [\d]+ service categories',
         f'Our system automatically categorizes workflows into {stats["categories_count"]} service categories'),

        # 更新任何 "2000+" 引用
        (r'2000\+', f'{stats["total_workflows"]:,}+'),
        (r'2,000\+', f'{stats["total_workflows"]:,}+'),

        # 搜索 X 个工作流
        (r'Search across [\d,]+ workflows', f'Search across {stats["total_workflows"]:,} workflows'),

        # 即时搜索 X 个工作流
        (r'Instant search across [\d,]+ workflows', f'Instant search across {stats["total_workflows"]:,} workflows'),
    ]

    # 应用所有替换
    updated_content = content
    replacements_made = 0

    for pattern, replacement in replacements:
        old_content = updated_content
        updated_content = re.sub(pattern, replacement, updated_content)
        if updated_content != old_content:
            replacements_made += 1

    # 写回文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"README.md 已使用当前统计信息更新：")
    print(f"  - 工作流总数：{stats['total_workflows']:,}")
    print(f"  - 活跃工作流：{stats['active_workflows']:,}")
    print(f"  - 节点总数：{stats['total_nodes']:,}")
    print(f"  - 唯一集成：{stats['unique_integrations']:,}")
    print(f"  - 类别：{stats['categories_count']}")
    print(f"  - 替换次数：{replacements_made}")

    return True


def main():
    """更新 README 统计信息的主函数。"""
    try:
        print("正在获取当前工作流统计信息...")
        stats = get_current_stats()

        if not stats:
            print("获取统计信息失败")
            sys.exit(1)

        print("正在更新 README.md...")
        success = update_readme_stats(stats)

        if success:
            print("README.md 已成功更新为最新统计信息！")
        else:
            print("更新 README.md 失败")
            sys.exit(1)

    except Exception as e:
        print(f"更新 README 统计信息时出错：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
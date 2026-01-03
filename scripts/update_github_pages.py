#!/usr/bin/env python3
"""
更新 GitHub Pages 文件
修复硬编码的时间戳并确保正确部署。
解决了问题 #115 和 #129。
"""

import json
import os
from datetime import datetime
from pathlib import Path
import re

def update_html_timestamp(html_file: str):
    """将 HTML 文件中的时间戳更新为当前日期。"""
    file_path = Path(html_file)

    if not file_path.exists():
        print(f"警告：未找到 {html_file}")
        return False

    # 读取 HTML 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取当前月份和年份
    current_date = datetime.now().strftime("%B %Y")

    # 替换硬编码的时间戳
    # 查找类似 "Last updated: Month Year" 的模式
    pattern = r'(<p class="footer-meta">Last updated:)\s*([^<]+)'
    replacement = f'\\1 {current_date}'

    updated_content = re.sub(pattern, replacement, content)

    # 另外添加一个带有精确时间戳的 meta 标签以便更好地跟踪
    if '<meta name="last-updated"' not in updated_content:
        timestamp_meta = f'    <meta name="last-updated" content="{datetime.now().isoformat()}">\n'
        updated_content = updated_content.replace('</head>', f'{timestamp_meta}</head>')

    # 将更新后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"✅ 已将 {html_file} 中的时间戳更新为：{current_date}")
    return True

def update_api_timestamp(api_dir: str):
    """更新 API JSON 文件中的时间戳。"""
    api_path = Path(api_dir)

    if not api_path.exists():
        api_path.mkdir(parents=True, exist_ok=True)

    # 创建或更新带有当前时间戳的元数据文件
    metadata = {
        "last_updated": datetime.now().isoformat(),
        "last_updated_readable": datetime.now().strftime("%B %d, %Y at %H:%M UTC"),
        "version": "2.0.1",
        "deployment_type": "github_pages"
    }

    metadata_file = api_path / 'metadata.json'
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ 创建元数据文件：{metadata_file}")

    # 如果存在则更新 stats.json
    stats_file = api_path / 'stats.json'
    if stats_file.exists():
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)

        stats['last_updated'] = datetime.now().isoformat()

        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)

        print(f"✅ 已使用新计数更新 stats.json")

    return True

def create_github_pages_config():
    """创建必要的 GitHub Pages 配置文件。"""

    # 为 Jekyll (GitHub Pages) 创建/更新 _config.yml
    config_content = """# GitHub Pages Configuration
theme: null
title: N8N Workflows Repository
description: Browse and search 2000+ n8n workflow automation templates
baseurl: "/n8n-workflows"
url: "https://zie619.github.io"

# Build settings
markdown: kramdown
exclude:
  - workflows/
  - scripts/
  - src/
  - "*.py"
  - requirements.txt
  - Dockerfile
  - docker-compose.yml
  - k8s/
  - helm/
  - Documentation/
  - context/
  - database/
  - static/
  - templates/
  - .github/
  - .devcontainer/
"""

    config_file = Path('docs/_config.yml')
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(config_content)
    print(f"✅ 创建 Jekyll 配置：{config_file}")

    # 创建 .nojekyll 文件以绕过 Jekyll 处理（适用于纯 HTML/JS 网站）
    nojekyll_file = Path('docs/.nojekyll')
    nojekyll_file.touch()
    print(f"✅ 创建 .nojekyll 文件：{nojekyll_file}")

    # 创建一个简单的 404.html 页面
    error_page_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 2rem;
        }
        h1 { font-size: 6rem; margin: 0; }
        p { font-size: 1.5rem; margin: 1rem 0; }
        a {
            display: inline-block;
            margin-top: 2rem;
            padding: 1rem 2rem;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 5px;
            transition: transform 0.2s;
        }
        a:hover { transform: scale(1.05); }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>Page not found</p>
        <p>The n8n workflows repository has been updated.</p>
        <a href="/n8n-workflows/">Go to Homepage</a>
    </div>
</body>
</html>"""

    error_file = Path('docs/404.html')
    with open(error_file, 'w', encoding='utf-8') as f:
        f.write(error_page_content)
    print(f"✅ 创建 404 页面：{error_file}")

def verify_github_pages_structure():
    """验证 GitHub Pages 部署所需的所有文件是否存在。"""

    required_files = [
        'docs/index.html',
        'docs/css/styles.css',
        'docs/js/app.js',
        'docs/js/search.js',
        'docs/api/search-index.json',
        'docs/api/stats.json',
        'docs/api/categories.json',
        'docs/api/integrations.json'
    ]

    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
            print(f"❌ 缺失：{file_path}")
        else:
            print(f"✅ 找到：{file_path}")

    if missing_files:
        print(f"\n⚠️  警告：缺失 {len(missing_files)} 个必需文件")
        print("运行以下命令生成缺失文件：")
        print("  python workflow_db.py --index --force")
        print("  python generate_search_index.py")
        return False

    print("\n✅ GitHub Pages 部署所需的所有文件均已存在")
    return True

def fix_base_url_references():
    """修复任何硬编码的 URL，使其在 GitHub Pages 中使用相对路径。"""

    # 更新 index.html 以使用相对路径
    index_file = Path('docs/index.html')
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 将绝对路径替换为相对路径
        replacements = [
            ('href="/css/', 'href="css/'),
            ('src="/js/', 'src="js/'),
            ('href="/api/', 'href="api/'),
            ('fetch("/api/', 'fetch("api/'),
            ("fetch('/api/", "fetch('api/"),
        ]

        for old, new in replacements:
            content = content.replace(old, new)

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ 已修复 index.html 中的 URL 引用")

    # 更新 JavaScript 文件
    js_files = ['docs/js/app.js', 'docs/js/search.js']
    for js_file in js_files:
        js_path = Path(js_file)
        if js_path.exists():
            with open(js_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 修复 API 端点引用
            content = content.replace("fetch('/api/", "fetch('api/")
            content = content.replace('fetch("/api/', 'fetch("api/')
            content = content.replace("'/api/", "'api/")
            content = content.replace('"/api/', '"api/')

            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已修复 {js_file} 中的 URL 引用")

def main():
    """更新 GitHub Pages 部署的主函数。"""

    print("🔧 GitHub Pages 更新脚本")
    print("=" * 50)

    # 步骤 1：更新时间戳
    print("\n📅 正在更新时间戳...")
    update_html_timestamp('docs/index.html')
    update_api_timestamp('docs/api')

    # 步骤 2：创建 GitHub Pages 配置
    print("\n⚙️  正在创建 GitHub Pages 配置...")
    create_github_pages_config()

    # 步骤 3：修复 URL 引用
    print("\n🔗 正在修复 URL 引用...")
    fix_base_url_references()

    # 步骤 4：验证结构
    print("\n✔️  正在验证部署结构...")
    if verify_github_pages_structure():
        print("\n✨ GitHub Pages 设置完成！")
        print("\n部署将在以下地址可用：")
        print("   https://zie619.github.io/n8n-workflows/")
        print("\n注意：推送到 GitHub 后，更改可能需要几分钟才能显示。")
    else:
        print("\n⚠️  部分文件缺失。请先生成这些文件。")

if __name__ == "__main__":
    main()
#!/bin/bash

# API功能测试脚本
# 用于测试N8N工作流文档平台的API端点功能
# 测试包括：搜索、分类、集成、筛选、分页和特定工作流查询

echo "🔍 正在测试API功能..."
echo "========================================="

# 测试搜索功能
# 目的：验证API能够根据关键词搜索工作流
# API端点：GET /api/workflows?search=Slack
# 参数：search=Slack - 搜索包含"Slack"的工作流
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取工作流数量
echo "1. 正在测试'Slack'搜索功能..."
results=$(curl -s "http://localhost:8000/api/workflows?search=Slack" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['workflows']))")
echo "   找到 $results 个包含'Slack'的工作流"

# 测试分类功能
# 目的：验证API能够获取所有工作流分类
# API端点：GET /api/categories
# 参数：无
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取分类数量
echo ""
echo "2. 正在测试分类API端点..."
categories=$(curl -s "http://localhost:8000/api/categories" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['categories']))")
echo "   找到 $categories 个分类"

# 测试集成功能
# 目的：验证API能够获取所有支持的集成
# API端点：GET /api/integrations
# 参数：无
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取集成数量
echo ""
echo "3. 正在测试集成API端点..."
integrations=$(curl -s "http://localhost:8000/api/integrations" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['integrations']))")
echo "   找到 $integrations 个集成"

# 测试筛选功能
# 目的：验证API能够按复杂度筛选工作流
# API端点：GET /api/workflows?complexity=high
# 参数：complexity=high - 筛选高复杂度的工作流
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取工作流数量
echo ""
echo "4. 正在测试按复杂度筛选功能..."
high_complex=$(curl -s "http://localhost:8000/api/workflows?complexity=high" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['workflows']))")
echo "   找到 $high_complex 个高复杂度工作流"

# 测试分页功能
# 目的：验证API能够支持分页查询工作流
# API端点：GET /api/workflows?page=2&per_page=10
# 参数：page=2 - 请求第2页数据；per_page=10 - 每页显示10条记录
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取分页信息
echo ""
echo "5. 正在测试分页功能..."
page2=$(curl -s "http://localhost:8000/api/workflows?page=2&per_page=10" | python3 -c "import sys, json; data=json.load(sys.stdin); print(f\"第 {data['page']} 页，共 {data['pages']} 页，当前页 {len(data['workflows'])} 条记录\")")
echo "   $page2"

# 测试特定工作流查询
# 目的：验证API能够根据ID获取特定工作流的详细信息
# API端点：GET /api/workflows/1
# 参数：URL路径中的1 - 工作流ID
# 处理方式：使用curl获取API响应，通过Python解析JSON并提取工作流名称
# 容错处理：如果API响应中没有'name'字段，显示'NOT FOUND'
echo ""
echo "6. 正在测试获取特定工作流..."
workflow=$(curl -s "http://localhost:8000/api/workflows/1" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data['name'] if 'name' in data else 'NOT FOUND')")
echo "   工作流：$workflow"

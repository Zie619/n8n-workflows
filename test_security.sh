#!/bin/bash
# -*- coding: utf-8 -*-

# 路径遍历保护测试脚本
# 用途：测试服务器是否能够有效防止路径遍历攻击
# 作者：系统管理员
# 创建日期：2026-01-03
# 说明：该脚本通过多种路径遍历攻击尝试，验证服务器是否能正确阻止这些攻击，
#       同时确保正常的下载功能不受影响。

# 路径遍历攻击（Path Traversal）是一种常见的Web安全漏洞，攻击者通过构造特殊的请求路径，
# 试图访问应用程序根目录之外的文件或目录，如系统文件（/etc/passwd）或配置文件等。

echo "🔒 测试路径遍历保护..."
echo "========================================="

# 定义多种路径遍历攻击尝试
# 这些攻击向量覆盖了常见的路径遍历技术，包括：
# - 基本的../和../../尝试
# - URL编码的路径遍历（%2F代表/，%5C代表\，%2E代表.）
# - 嵌套多个../尝试
# - 双斜杠绕过技巧
# - Windows风格的路径分隔符
# - SSH私钥等敏感文件访问

declare -a attacks=(
  "../api_server.py"             # 基本的父目录遍历
  "../../etc/passwd"             # 尝试访问系统密码文件
  "..%2F..%2Fapi_server.py"      # URL编码的父目录遍历（/）
  "..%5C..%5Capi_server.py"      # URL编码的父目录遍历（\）
  "%2e%2e%2fapi_server.py"       # URL编码的.和/组合
  "../../../../../../../etc/passwd" # 深度嵌套的父目录遍历
  "....//....//api_server.py"     # 双斜杠绕过技巧
  "..;/api_server.py"            # 分号绕过技巧
  "..\api_server.py"             # Windows风格路径分隔符
  "~/.ssh/id_rsa"                # 尝试访问SSH私钥
)

# 遍历所有攻击向量进行测试
for attack in "${attacks[@]}"; do
  # 使用curl命令发送请求并获取HTTP响应码
  # 参数说明：
  # -s：静默模式，不显示进度和错误信息
  # -o /dev/null：将响应内容丢弃到空设备
  # -w "%{http_code}"：仅输出HTTP响应码
  # "http://localhost:8000/api/workflows/$attack/download"：测试URL
  response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/api/workflows/$attack/download")
  
  # 检查响应码：
  # 400 Bad Request：服务器识别到请求格式错误（如包含恶意路径）
  # 404 Not Found：服务器未找到请求的资源
  # 这两种响应都表示攻击被成功阻止
  if [ "$response" == "400" ] || [ "$response" == "404" ]; then
    echo "✅ 已阻止: $attack (响应: $response)"
  else
    echo "❌ 未能阻止: $attack (响应: $response)"
  fi
done

echo ""
echo "🔍 测试有效下载..."
echo "========================================="

# 测试正常的文件下载功能是否仍然工作
# 确保安全防护措施不会影响合法用户的正常操作
response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/api/workflows/0720_Schedule_Filter_Create_Scheduled.json/download")
if [ "$response" == "200" ]; then
  echo "✅ 有效下载正常工作 (响应: $response)"
else
  echo "❌ 有效下载失败 (响应: $response)"
fi

# 使用说明：
# 1. 确保目标服务器正在运行（http://localhost:8000）
# 2. 确保服务器实现了路径遍历保护功能
# 3. 运行脚本：bash test_security.sh
# 4. 检查输出结果，确认所有攻击尝试都被阻止

# 预期结果：
# - 所有路径遍历攻击尝试都应返回400或404响应
# - 正常的文件下载应返回200响应

# 注意事项：
# - 该脚本仅测试了部分常见的路径遍历攻击向量
# - 实际部署中应使用更全面的安全测试工具
# - 服务器应配置适当的访问控制和输入验证

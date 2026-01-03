#!/bin/bash
# -*- coding: utf-8 -*-

# N8N工作流健康检查脚本
# 用途：检查N8N工作流服务的健康状态和可用性
# 作者：本地化团队
# 创建日期：2026-01-03
# 
# 关于N8N：
# N8N是一款开源的自动化工作流工具，允许用户通过图形界面构建自动化工作流
# 该脚本用于监控N8N服务的运行状态，确保API、主页面和文档页面都能正常访问
# 
# 使用方法：
# 1. 默认检查localhost:8000：./scripts/health-check.sh
# 2. 检查自定义端点：./scripts/health-check.sh http://your-n8n-server:8000
# 
# 检查内容包括：
# - API统计端点响应状态
# - 工作流统计信息（总工作流数、活跃工作流数、唯一集成数）
# - 主页面可访问性
# - API文档页面可访问性

# 设置Shell严格模式：
# -e：命令失败时立即退出
# -u：使用未定义变量时抛出错误
# -o pipefail：管道中任何命令失败时整个管道失败
set -euo pipefail

# 默认检查端点，如未提供则使用localhost:8000
ENDPOINT="${1:-http://localhost:8000}"
# 最大重试次数
MAX_ATTEMPTS=5
# 每个请求的超时时间（秒）
TIMEOUT=10

# 输出颜色定义
# ANSI颜色代码，用于美化输出内容
RED='\033[0;31m'      # 红色 - 用于错误信息
GREEN='\033[0;32m'    # 绿色 - 用于成功信息
YELLOW='\033[1;33m'   # 黄色 - 用于警告信息
BLUE='\033[0;34m'     # 蓝色 - 用于日志信息
NC='\033[0m'          # 重置颜色 - 恢复默认终端颜色

# 日志函数：输出带时间戳的普通日志信息
# 参数：要输出的日志内容
log() {
    # -e 启用转义字符解析，使颜色代码生效
    echo -e "${BLUE}[\$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

# 警告函数：输出黄色警告信息
# 参数：要输出的警告内容
warn() {
    echo -e "${YELLOW}[警告]${NC} $1"
}

# 错误函数：输出红色错误信息
# 参数：要输出的错误内容
error() {
    echo -e "${RED}[错误]${NC} $1"
}

# 成功函数：输出绿色成功信息
# 参数：要输出的成功内容
success() {
    echo -e "${GREEN}[成功]${NC} $1"
}

# 检查curl命令是否可用
# 该脚本使用curl进行HTTP请求，因此需要确保curl已安装
if ! command -v curl &> /dev/null; then
    # command -v curl: 检查curl命令是否存在
    # &> /dev/null: 将所有输出（标准输出和标准错误）重定向到空设备（不显示任何信息）
    error "需要curl命令但未安装，请先安装curl"
    exit 1
fi

# 开始健康检查过程
log "开始对 $ENDPOINT 进行健康检查"

# 测试基础连接性
# 循环执行健康检查，最多尝试MAX_ATTEMPTS次
for attempt in $(seq 1 $MAX_ATTEMPTS); do
    log "健康检查尝试 $attempt/$MAX_ATTEMPTS"
    
    # 测试API统计端点
    # curl命令参数说明：
    # -s：静默模式，不显示进度条和错误信息
    # -w "%{http_code}"：在响应内容后追加HTTP状态码
    # -o /tmp/health_response：将响应内容保存到临时文件
    # --connect-timeout $TIMEOUT：设置连接超时时间
    # 2>/dev/null：将错误信息重定向到空设备
    if response=$(curl -s -w "%{http_code}" -o /tmp/health_response --connect-timeout $TIMEOUT "$ENDPOINT/api/stats" 2>/dev/null); then
        # 从响应中提取HTTP状态码（最后3个字符）
        # tail -c 4：取最后4个字符（包含一个换行符）
        # head -c 3：取前3个字符（实际的HTTP状态码）
        http_code=$(echo "$response" | tail -c 4 | head -c 3)
        
        if [[ "$http_code" == "200" ]]; then
            success "API响应正常 (HTTP $http_code)"
            
            # 解析并显示统计信息
            # 检查jq工具是否可用（用于解析JSON数据）
            if command -v jq &> /dev/null; then
                # 读取临时文件中的响应内容
                stats=$(cat /tmp/health_response)
                
                # 使用jq解析JSON数据：
                # -r：输出原始字符串（不包含引号）
                # // "N/A"：如果字段不存在，则返回"N/A"
                total=$(echo "$stats" | jq -r '.total // "N/A"')          # 总工作流数
                active=$(echo "$stats" | jq -r '.active // "N/A"')        # 活跃工作流数
                integrations=$(echo "$stats" | jq -r '.unique_integrations // "N/A"')  # 唯一集成数
                
                log "数据库状态:"
                log "  - 总工作流数: $total"
                log "  - 活跃工作流数: $active"
                log "  - 唯一集成数: $integrations"
            else
                # 如果jq不可用，只记录基本信息
                log "无法解析统计信息：需要jq工具"
            fi
            
            # 测试主页面可访问性
            # curl参数说明：
            # -f：失败时返回非零状态码（HTTP 400或更高）
            # > /dev/null：将响应内容重定向到空设备（只关注是否能访问，不关心内容）
            if curl -s -f --connect-timeout $TIMEOUT "$ENDPOINT" > /dev/null; then
                success "主页面可访问"
            else
                warn "主页面不可访问"
            fi
            
            # 测试API文档页面可访问性
            if curl -s -f --connect-timeout $TIMEOUT "$ENDPOINT/docs" > /dev/null; then
                success "API文档页面可访问"
            else
                warn "API文档页面不可访问"
            fi
            
            # 清理临时文件
            # rm -f：强制删除文件，即使文件不存在也不报错
            rm -f /tmp/health_response
            
            success "所有健康检查通过！"
            exit 0
        else
            warn "API返回了HTTP $http_code状态码"
        fi
    else
        warn "无法连接到 $ENDPOINT"
    fi
    
    # 如果不是最后一次尝试，则等待一段时间后重试
    if [[ $attempt -lt $MAX_ATTEMPTS ]]; then
        log "等待5秒后重试..."
        sleep 5  # 暂停5秒
    fi
done

# 所有尝试都失败后，清理临时文件
rm -f /tmp/health_response

error "经过 $MAX_ATTEMPTS 次尝试后，健康检查失败"
exit 1
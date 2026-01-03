#!/bin/bash

# N8N工作流文档 - Docker容器运行器
# 增强版，具有更好的跨平台支持和错误处理

# 设置shell选项：
# -e: 发生错误时立即退出
# -u: 遇到未定义变量时退出
# -o pipefail: 管道中任何命令失败时，整个管道返回失败状态
set -euo pipefail

# 输出颜色设置
# ANSI颜色代码，用于美化终端输出
GREEN='\033[0;32m'  # 绿色：用于成功消息
BLUE='\033[0;34m'   # 蓝色：用于普通信息
YELLOW='\033[1;33m' # 黄色：用于警告消息
RED='\033[0;31m'    # 红色：用于错误消息
NC='\033[0m'        # 重置颜色：恢复默认终端颜色

# 日志函数：输出蓝色INFO信息
# 参数：$1 - 要输出的日志消息
log() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# 成功函数：输出绿色SUCCESS信息
# 参数：$1 - 要输出的成功消息
success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# 警告函数：输出黄色WARNING信息
# 参数：$1 - 要输出的警告消息
warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# 错误函数：输出红色ERROR信息并退出脚本
# 参数：$1 - 要输出的错误消息
# 返回：退出脚本，状态码为1
error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# 检查先决条件：确保Docker和Docker Compose已安装
# command -v: 检查命令是否存在于系统路径中
# &> /dev/null: 将标准输出和标准错误重定向到空设备（不显示任何输出）
if ! command -v docker &> /dev/null; then
    error "Docker未安装。请先安装Docker。"
fi

if ! docker compose version &> /dev/null; then
    error "Docker Compose不可用。请安装Docker Compose。"
fi

log "正在启动N8N工作流文档平台..."

# 构建并启动Docker容器
# docker compose up: 启动Docker Compose定义的所有服务
# -d: 后台运行模式（daemon模式）
# --build: 总是重新构建镜像，确保使用最新的代码
if ! docker compose up -d --build; then
    error "启动Docker容器失败"
fi

# 等待应用程序启动
# 先等待10秒，给应用程序足够的初始化时间
log "正在等待应用程序启动..."
sleep 10

# 健康检查：确保应用程序能够正常响应请求
# 这一步是为了避免在应用程序尚未完全启动时就通知用户
max_attempts=12  # 最大尝试次数：最多尝试12次
attempt=1        # 当前尝试次数：从第1次开始

# while循环：进行多次健康检查直到成功或达到最大尝试次数
while [[ $attempt -le $max_attempts ]]; do
    log "健康检查尝试 $attempt/$max_attempts"
    
    # curl命令：检查API端点是否可用
    # -s: 静默模式，不显示进度条和错误信息
    # -f: 失败时返回非零状态码（HTTP状态码>=400时认为失败）
    # > /dev/null 2>&1: 将所有输出重定向到空设备（不显示任何内容）
    if curl -s -f http://localhost:8000/api/stats > /dev/null 2>&1; then
        success "应用程序已准备就绪！"
        break  # 健康检查通过，退出循环
    fi
    
    # 如果达到最大尝试次数，发出警告并退出循环
    if [[ $attempt -eq $max_attempts ]]; then
        warn "应用程序可能尚未完全准备就绪"
        break
    fi
    
    sleep 5          # 等待5秒后再次尝试
    ((attempt++))    # 增加尝试次数
done

# 显示应用程序信息：向用户提供使用指南
# 包括访问URL、容器状态和常用命令
success "N8N工作流文档平台正在运行！"
echo  # 空行，用于美化输出
echo "🌐 访问URL："
echo "   主界面：http://localhost:8000"
echo "   API文档：http://localhost:8000/docs"
echo "   API统计：http://localhost:8000/api/stats"
echo
echo "📊 容器状态："
# docker compose ps: 显示所有容器的运行状态
docker compose ps
echo
echo "📝 查看日志：docker compose logs -f"
echo "🛑 停止：docker compose down"

# 根据操作系统自动打开浏览器
# 支持macOS、Windows和Linux三大主流操作系统
# 参数：无（内部使用固定URL）
# 返回：无（成功时打开浏览器，失败时发出警告）
open_browser() {
    local url="http://localhost:8000"  # 要打开的应用程序URL
    
    # case语句：根据操作系统类型执行不同的浏览器打开命令
    # $OSTYPE是Shell内置变量，包含当前操作系统类型
    case "$OSTYPE" in
        darwin*)  # macOS操作系统
            # macOS使用open命令打开URL
            if command -v open &> /dev/null; then
                log "正在macOS上打开浏览器..."
                # 尝试打开浏览器，如果失败则发出警告
                # 2>/dev/null: 将错误输出重定向到空设备
                # ||: 如果前一个命令失败，则执行后面的命令
                open "$url" 2>/dev/null || warn "无法自动打开浏览器"
            fi
            ;;
        msys*|cygwin*|win*)  # Windows操作系统
            # Windows使用start命令打开URL
            log "正在Windows上打开浏览器..."
            start "$url" 2>/dev/null || warn "无法自动打开浏览器"
            ;;
        linux*)  # Linux操作系统
            # Linux需要检查显示器是否可用，并使用xdg-open命令
            # ${DISPLAY:-}: 如果DISPLAY变量未定义则使用空值
            # -n: 检查变量是否非空（即是否有可用的图形界面）
            if [[ -n "${DISPLAY:-}" ]] && command -v xdg-open &> /dev/null; then
                log "正在Linux上打开浏览器..."
                xdg-open "$url" 2>/dev/null || warn "无法自动打开浏览器"
            else
                log "未检测到显示器或xdg-open不可用"
            fi
            ;;
        *)  # 未知操作系统
            warn "未知操作系统：$OSTYPE"
            ;;
    esac
}

# 尝试自动打开浏览器
# 这一步是为了提升用户体验，让用户无需手动输入URL
open_browser

log "设置完成！应用程序现在应该可以在浏览器中访问了。"
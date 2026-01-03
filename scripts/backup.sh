#!/bin/bash

# N8N工作流备份脚本
# 用途：备份N8N工作流数据库、配置文件和日志
# 使用方法：./scripts/backup.sh [备份名称]
# 如果不指定备份名称，将自动使用当前时间戳作为名称

# 设置shell选项
# -e：当命令执行失败时立即退出脚本
# -u：当使用未定义的变量时立即退出脚本
# -o pipefail：当管道中的任何命令失败时，将整个管道视为失败
set -euo pipefail

# 获取脚本所在目录的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 获取项目根目录的绝对路径
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
# 设置备份名称，如果未提供参数则使用时间戳
BACKUP_NAME="${1:-$(date +%Y%m%d_%H%M%S)}"
# 设置备份目录
BACKUP_DIR="$PROJECT_DIR/backups"
# 设置完整备份路径
BACKUP_PATH="$BACKUP_DIR/backup_$BACKUP_NAME"

# 输出颜色定义
GREEN='\033[0;32m'  # 绿色，用于成功消息
BLUE='\033[0;34m'   # 蓝色，用于日志消息
NC='\033[0m'        # 重置颜色

# 日志输出函数
# 参数：$1 - 要输出的日志消息
log() {
    echo -e "${BLUE}[\$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

# 成功消息输出函数
# 参数：$1 - 要输出的成功消息
success() {
    echo -e "${GREEN}[成功]${NC} $1"
}

# 创建备份目录
# mkdir -p：递归创建目录，若目录已存在则不报错
mkdir -p "$BACKUP_PATH"

log "正在创建备份: $BACKUP_NAME"

# 备份数据库
if [[ -f "$PROJECT_DIR/database/workflows.db" ]]; then
    log "正在备份数据库..."
    cp "$PROJECT_DIR/database/workflows.db" "$BACKUP_PATH/workflows.db"
    success "数据库已备份"
fi

# 备份配置文件
log "正在备份配置文件..."
# 备份所有YAML配置文件
cp -r "$PROJECT_DIR"/*.yml "$BACKUP_PATH/" 2>/dev/null || true
# 备份所有环境变量文件
cp "$PROJECT_DIR"/.env* "$BACKUP_PATH/" 2>/dev/null || true
# 备份Kubernetes配置
cp -r "$PROJECT_DIR"/k8s "$BACKUP_PATH/" 2>/dev/null || true
# 备份Helm配置
cp -r "$PROJECT_DIR"/helm "$BACKUP_PATH/" 2>/dev/null || true

# 备份日志（仅保留最近7天）
if [[ -d "$PROJECT_DIR/logs" ]]; then
    log "正在备份最近日志..."
    # 查找并复制最近7天内修改的日志文件
    find "$PROJECT_DIR/logs" -name "*.log" -mtime -7 -exec cp {} "$BACKUP_PATH/" \; 2>/dev/null || true
fi

# 创建备份归档文件
log "正在创建备份归档文件..."
cd "$BACKUP_DIR"
# 使用tar创建压缩归档文件
# -c：创建新归档
# -z：使用gzip压缩
# -f：指定归档文件名
tar -czf "backup_$BACKUP_NAME.tar.gz" "backup_$BACKUP_NAME"
# 删除临时备份目录
rm -rf "backup_$BACKUP_NAME"

# 清理旧备份（保留最近10个）
# 1. 查找所有备份文件并按修改时间排序
# 2. 从第11个开始删除旧备份
find "$BACKUP_DIR" -name "backup_*.tar.gz" -type f -printf '%T@ %p\n' | \
    sort -rn | tail -n +11 | cut -d' ' -f2- | xargs rm -f

success "备份已创建: $BACKUP_DIR/backup_$BACKUP_NAME.tar.gz"
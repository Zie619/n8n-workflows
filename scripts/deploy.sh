#!/bin/bash

# N8N工作流生产部署脚本
# 用途：部署N8N工作流到不同环境
# 使用方法：./scripts/deploy.sh [环境]
# 环境选项：development（开发环境）, staging（预生产环境）, production（生产环境）

# 设置shell选项
# -e：当命令执行失败时立即退出脚本
# -u：当使用未定义的变量时立即退出脚本
# -o pipefail：当管道中的任何命令失败时，将整个管道视为失败
set -euo pipefail

# 配置部分
# 获取脚本所在目录的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 获取项目根目录的绝对路径
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
# 设置部署环境，如果未提供参数则默认使用production
ENVIRONMENT="${1:-production}"
# 设置Docker镜像名称，包含环境标识
DOCKER_IMAGE="workflows-doc:${ENVIRONMENT}"

# 输出颜色定义
RED='\033[0;31m'    # 红色，用于错误消息
GREEN='\033[0;32m'  # 绿色，用于成功消息
YELLOW='\033[1;33m' # 黄色，用于警告消息
BLUE='\033[0;34m'   # 蓝色，用于日志消息
NC='\033[0m'        # 重置颜色

# 日志输出函数
# 参数：$1 - 要输出的日志消息
log() {
    echo -e "${BLUE}[\$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

# 警告消息输出函数
# 参数：$1 - 要输出的警告消息
warn() {
    echo -e "${YELLOW}[警告]${NC} $1"
}

# 错误消息输出函数
# 参数：$1 - 要输出的错误消息
error() {
    echo -e "${RED}[错误]${NC} $1"
    exit 1
}

# 成功消息输出函数
# 参数：$1 - 要输出的成功消息
success() {
    echo -e "${GREEN}[成功]${NC} $1"
}

# 检查部署前提条件
check_prerequisites() {
    log "正在检查部署前提条件..."
    
    # 检查Docker是否安装
    if ! command -v docker &> /dev/null; then
        error "Docker未安装"
    fi
    
    # 检查Docker Compose是否安装
    if ! docker compose version &> /dev/null; then
        error "Docker Compose未安装"
    fi
    
    # 检查Docker守护进程是否正在运行
    if ! docker info &> /dev/null; then
        error "Docker守护进程未运行"
    fi
    
    success "前提条件检查通过"
}

# 验证部署环境
validate_environment() {
    log "正在验证环境: $ENVIRONMENT"
    
    case $ENVIRONMENT in
        development|staging|production)
            log "环境 '$ENVIRONMENT' 有效"
            ;;
        *)
            error "无效的环境: $ENVIRONMENT。请使用: development, staging 或 production"
            ;;
    esac
}

# 构建Docker镜像
build_image() {
    log "正在为 $ENVIRONMENT 环境构建Docker镜像..."
    
    cd "$PROJECT_DIR"
    
    if [[ "$ENVIRONMENT" == "development" ]]; then
        # 开发环境使用默认构建目标
        docker build -t "$DOCKER_IMAGE" .
    else
        # 预生产和生产环境使用production构建目标
        docker build -t "$DOCKER_IMAGE" --target production .
    fi
    
    success "Docker镜像构建成功: $DOCKER_IMAGE"
}

# 使用Docker Compose部署
deploy_docker_compose() {
    log "正在使用Docker Compose部署..."
    
    cd "$PROJECT_DIR"
    
    # 停止并移除现有容器
    if [[ "$ENVIRONMENT" == "development" ]]; then
        # 开发环境使用开发配置文件
        docker compose -f docker-compose.yml -f docker-compose.dev.yml down --remove-orphans
        docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
    else
        # 预生产和生产环境使用生产配置文件
        docker compose -f docker-compose.yml -f docker-compose.prod.yml down --remove-orphans
        docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
    fi
    
    success "Docker Compose部署完成"
}

# 部署到Kubernetes
deploy_kubernetes() {
    log "正在部署到Kubernetes..."
    
    if ! command -v kubectl &> /dev/null; then
        error "kubectl未安装"
    fi
    
    cd "$PROJECT_DIR"
    
    # 应用Kubernetes配置文件
    kubectl apply -f k8s/namespace.yaml    # 创建命名空间
    kubectl apply -f k8s/configmap.yaml     # 创建配置映射
    kubectl apply -f k8s/deployment.yaml    # 创建部署
    kubectl apply -f k8s/service.yaml       # 创建服务
    
    if [[ "$ENVIRONMENT" == "production" ]]; then
        kubectl apply -f k8s/ingress.yaml   # 生产环境创建Ingress
    fi
    
    # 等待部署完成
    kubectl rollout status deployment/workflows-docs -n n8n-workflows --timeout=300s
    
    success "Kubernetes部署完成"
}

# 使用Helm部署
deploy_helm() {
    log "正在使用Helm部署..."
    
    if ! command -v helm &> /dev/null; then
        error "Helm未安装"
    fi
    
    cd "$PROJECT_DIR"
    
    local release_name="workflows-docs-$ENVIRONMENT"
    local values_file="helm/workflows-docs/values-$ENVIRONMENT.yaml"
    
    if [[ -f "$values_file" ]]; then
        # 使用环境特定的values文件部署
        helm upgrade --install "$release_name" ./helm/workflows-docs \
            --namespace n8n-workflows \
            --create-namespace \
            --values "$values_file" \
            --wait --timeout=300s
    else
        warn "未找到values文件 $values_file，将使用默认值"
        helm upgrade --install "$release_name" ./helm/workflows-docs \
            --namespace n8n-workflows \
            --create-namespace \
            --wait --timeout=300s
    fi
    
    success "Helm部署完成"
}

# 健康检查
health_check() {
    log "正在执行健康检查..."
    
    local max_attempts=30  # 最大尝试次数
    local attempt=1        # 当前尝试次数
    local url="http://localhost:8000/api/stats"  # 默认健康检查URL
    
    if [[ "$ENVIRONMENT" == "production" ]]; then
        url="https://workflows.yourdomain.com/api/stats"  # 生产环境URL，请根据实际情况修改
    fi
    
    while [[ $attempt -le $max_attempts ]]; do
        log "健康检查尝试 $attempt/$max_attempts..."
        
        # 使用curl检查URL是否可访问
        if curl -f -s "$url" &> /dev/null; then
            success "应用程序健康！"
            return 0
        fi
        
        sleep 10  # 等待10秒后重试
        ((attempt++))
    done
    
    error "健康检查在 $max_attempts 次尝试后失败"
}

# 清理旧资源
cleanup() {
    log "正在清理旧资源..."
    
    # 删除悬空的Docker镜像
    docker image prune -f
    
    # 删除未使用的Docker卷
    docker volume prune -f
    
    success "清理完成"
}

# 主部署函数
deploy() {
    log "正在开始 $ENVIRONMENT 环境的部署过程..."
    
    # 执行前置检查和环境验证
    check_prerequisites
    validate_environment
    
    # 根据环境和可用工具选择部署方法
    if command -v kubectl &> /dev/null && [[ "$ENVIRONMENT" == "production" ]]; then
        # 生产环境优先使用Kubernetes部署
        if command -v helm &> /dev/null; then
            # 如果Helm可用，使用Helm部署
            deploy_helm
        else
            # 否则使用kubectl直接部署
            deploy_kubernetes
        fi
    else
        # 非生产环境使用Docker Compose部署
        build_image
        deploy_docker_compose
    fi
    
    # 执行健康检查和资源清理
    health_check
    cleanup
    
    success "部署成功完成！"
    
    # 显示部署信息
    case $ENVIRONMENT in
        development)
            log "应用程序可访问地址: http://localhost:8000"
            log "API文档地址: http://localhost:8000/docs"
            ;;
        staging)
            log "应用程序可访问地址: http://workflows-staging.yourdomain.com"
            ;;
        production)
            log "应用程序可访问地址: https://workflows.yourdomain.com"
            ;;
    esac
}

# 回滚函数
rollback() {
    log "正在回滚部署..."
    
    if command -v kubectl &> /dev/null; then
        kubectl rollout undo deployment/workflows-docs -n n8n-workflows
        kubectl rollout status deployment/workflows-docs -n n8n-workflows --timeout=300s
    else
        cd "$PROJECT_DIR"
        docker compose down
        # 如果有备份则从备份恢复
        if [[ -f "database/workflows.db.backup" ]]; then
            cp database/workflows.db.backup database/workflows.db
        fi
        deploy_docker_compose
    fi
    
    success "回滚完成"
}

# 显示使用信息
usage() {
    cat << EOF
N8N工作流文档 - 部署脚本

使用方法: $0 [选项] [环境]

环境选项:
    development    开发环境（默认配置）
    staging        预生产环境（接近生产环境配置）
    production     生产环境（完整的安全性和性能配置）

可用选项:
    --rollback     回滚到上一次部署
    --cleanup      仅清理（删除旧资源）
    --health       仅执行健康检查
    --help         显示此帮助信息

示例:
    $0 development                  # 部署到开发环境
    $0 production                   # 部署到生产环境
    $0 --rollback production        # 回滚生产环境部署
    $0 --health                     # 检查应用程序健康状态

EOF
}

# 解析命令行参数
main() {
    case "${1:-}" in
        --help|-h)
            usage
            exit 0
            ;;
        --rollback)
            ENVIRONMENT="${2:-production}"
            rollback
            exit 0
            ;;
        --cleanup)
            cleanup
            exit 0
            ;;
        --health)
            health_check
            exit 0
            ;;
        "")
            deploy
            ;;
        *)
            ENVIRONMENT="$1"
            deploy
            ;;
    esac
}

# 执行主函数并传递所有参数
main "$@"
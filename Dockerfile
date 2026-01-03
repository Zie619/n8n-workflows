# 构建N8N工作流文档API的Docker镜像
# 遵循安全最佳实践，包括非root用户运行、最小化依赖等

# 使用官方Python运行时作为基础镜像 - 选择稳定安全的版本
# python:3.11-slim-bookworm 提供了较小的镜像大小和良好的安全性
FROM python:3.11-slim-bookworm AS base

# 安全措施：先设置非root用户
# 创建appuser组和用户，用于后续以最小权限运行应用
RUN groupadd -g 1001 appuser && \
    useradd -m -u 1001 -g appuser appuser

# 设置环境变量以提高安全性和性能
ENV PYTHONUNBUFFERED=1 \
    # 禁用Python缓冲输出，确保日志实时显示
    PYTHONDONTWRITEBYTECODE=1 \
    # 防止生成.pyc文件，减少镜像大小
    PYTHONHASHSEED=random \
    # 使用随机哈希种子，提高安全性
    PIP_NO_CACHE_DIR=1 \
    # 禁用pip缓存，减少镜像大小
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # 禁用pip版本检查，加速构建
    PIP_DEFAULT_TIMEOUT=100 \
    # 增加pip超时时间，避免网络问题导致构建失败
    PIP_ROOT_USER_ACTION=ignore \
    # 忽略root用户警告
    DEBIAN_FRONTEND=noninteractive \
    # 设置非交互式前端，避免apt-get询问
    PYTHONIOENCODING=utf-8 
    # 设置Python编码为UTF-8，支持中文


# 安装安全更新和ARM64构建依赖
# 更新系统包并安装必要的构建工具
RUN apt-get update && \
    apt-get upgrade -y && \
    # 安装安全更新
    apt-get install -y --no-install-recommends \
    ca-certificates \
    # 安装CA证书，用于HTTPS连接
    gcc \
    # 安装编译器，用于构建Python扩展
    python3-dev \
    # 安装Python开发文件
    && apt-get autoremove -y \
    # 自动移除不再需要的依赖
    && apt-get clean \
    # 清理apt缓存
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache \
    # 删除临时文件和缓存，减少镜像大小
    && update-ca-certificates
    # 更新CA证书，确保HTTPS连接安全

# 创建应用目录并设置正确权限
WORKDIR /app
RUN chown -R appuser:appuser /app
    # 将/app目录所有权设置为appuser

# 复制requirements.txt文件，使用chown确保appuser有读取权限
COPY --chown=appuser:appuser requirements.txt .

# 安装Python依赖，采用安全加固措施
# 不固定版本以获得更好的ARM64兼容性
RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    # 更新pip、setuptools和wheel到最新版本
    python -m pip install --no-cache-dir -r requirements.txt && \
    # 安装项目依赖
    find /usr/local -type f -name '*.pyc' -delete && \
    find /usr/local -type d -name '__pycache__' -delete
    # 删除编译后的Python文件，减少镜像大小

# 复制应用程序代码，并设置正确的所有权
COPY --chown=appuser:appuser . .

# 创建必要的目录并设置正确的权限
RUN mkdir -p /app/database /app/workflows /app/static /app/src && \
    # 创建数据库、工作流、静态文件和源代码目录
    chown -R appuser:appuser /app
    # 确保所有目录都属于appuser

# 安全措施：切换到非root用户
# 从这里开始，所有操作都将以appuser身份执行
USER appuser

# 健康检查配置
# 每30秒检查一次，超时时间10秒，启动后5秒开始检查，最多重试3次
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/api/stats')" || exit 1
    # 通过访问/api/stats端点检查应用是否正常运行

# 暴露端口（信息性）
# 实际端口映射由Docker运行时控制
EXPOSE 8000

# 安全措施：以最小权限运行应用
# 使用python -u确保日志实时输出
CMD ["python", "-u", "run.py", "--host", "0.0.0.0", "--port", "8000"]
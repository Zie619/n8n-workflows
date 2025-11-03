# Use official Python runtime as base image - latest secure version
FROM python:3.12.7-slim-bookworm AS base

# Security: Set up non-root user first
RUN groupadd -g 1001 appuser && \
    useradd -m -u 1001 -g appuser appuser

# Set environment variables for security and performance
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_ROOT_USER_ACTION=ignore \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONIOENCODING=utf-8

# Install security updates and minimal dependencies
# Use specific versions to avoid CVEs
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates=20230311 \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache \
    && update-ca-certificates

# Create app directory with correct permissions
WORKDIR /app
RUN chown -R appuser:appuser /app

# Copy requirements as root to ensure they're readable
COPY --chown=appuser:appuser requirements.txt .

# Install Python dependencies with security hardening
RUN python -m pip install --no-cache-dir --upgrade pip==24.3.1 setuptools==75.3.0 wheel==0.44.0 && \
    python -m pip install --no-cache-dir --no-compile -r requirements.txt && \
    find /usr/local -type f -name '*.pyc' -delete && \
    find /usr/local -type d -name '__pycache__' -delete

# Copy application code with correct ownership
COPY --chown=appuser:appuser . .

# Create necessary directories with correct permissions
RUN mkdir -p /app/database /app/workflows /app/static /app/src && \
    chown -R appuser:appuser /app

# Security: Switch to non-root user
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/api/stats')" || exit 1

# Expose port (informational)
EXPOSE 8000

# Security: Run with minimal privileges
CMD ["python", "-u", "run.py", "--host", "0.0.0.0", "--port", "8000"]
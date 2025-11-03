# Use official Python runtime as base image - stable and secure version
FROM python:3.11-slim-bookworm AS base

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
    DEBIAN_FRONTEND=noninteractive

# Install security updates and minimal dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && update-ca-certificates

# Create app directory with correct permissions
WORKDIR /app
RUN chown -R appuser:appuser /app

# Copy requirements as root to ensure they're readable
COPY --chown=appuser:appuser requirements.txt .

# Install Python dependencies as root for system-wide access
RUN pip install --no-cache-dir --upgrade pip==24.3.1 && \
    pip install --no-cache-dir -r requirements.txt

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
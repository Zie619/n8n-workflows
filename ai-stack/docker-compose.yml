# =============================================================================
# Turnkey Local AI Automation Stack
# n8n (orchestration) + Agent Zero (agent runtime) + ComfyUI (media generation)
# =============================================================================
# Usage: docker compose up -d
# URLs:
#   - n8n:        http://localhost:5678
#   - Agent Zero: http://localhost:50080
#   - ComfyUI:    http://localhost:8188
# =============================================================================

services:
  # ---------------------------------------------------------------------------
  # n8n - Workflow Automation Engine (The Conductor)
  # ---------------------------------------------------------------------------
  n8n:
    image: n8nio/n8n:latest
    container_name: ai-stack-n8n
    ports:
      - "5678:5678"
    environment:
      # Core configuration
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      # Webhook URL - critical for correct webhook URLs in editor
      - WEBHOOK_URL=http://localhost:5678
      # Timezone
      - GENERIC_TIMEZONE=${TZ:-America/Los_Angeles}
      - TZ=${TZ:-America/Los_Angeles}
      # Execution settings
      - EXECUTIONS_DATA_PRUNE=true
      - EXECUTIONS_DATA_MAX_AGE=168
      # Allow calling local services
      - N8N_PAYLOAD_SIZE_MAX=256
    volumes:
      - ./data/n8n:/home/node/.n8n
      - ./shared:/shared
    networks:
      - ai-stack-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:5678/healthz || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  # ---------------------------------------------------------------------------
  # Agent Zero - AI Agent Runtime & UI
  # ---------------------------------------------------------------------------
  agent-zero:
    image: frdel/agent-zero-run:latest
    container_name: ai-stack-agent-zero
    ports:
      # Agent Zero web UI is on container port 80
      - "50080:80"
    environment:
      - TZ=${TZ:-America/Los_Angeles}
    volumes:
      - ./shared:/shared
      - ./data/agent-zero:/app/data
    networks:
      - ai-stack-network
    restart: unless-stopped
    depends_on:
      - n8n

  # ---------------------------------------------------------------------------
  # ComfyUI - AI Image/Video Generation
  # ---------------------------------------------------------------------------
  # Using a well-maintained community image
  # GPU support requires NVIDIA Container Toolkit
  comfyui:
    image: aidockorg/comfyui-cuda:latest
    container_name: ai-stack-comfyui
    ports:
      - "8188:8188"
    environment:
      - CLI_ARGS=--listen 0.0.0.0 --port 8188
    volumes:
      # Model storage (checkpoints, loras, etc.)
      - ./shared/comfyui/models:/comfyui/models
      # Output directory
      - ./shared/comfyui/output:/comfyui/output
      # Input directory
      - ./shared/comfyui/input:/comfyui/input
      # Custom nodes
      - ./shared/comfyui/custom_nodes:/comfyui/custom_nodes
    networks:
      - ai-stack-network
    # GPU support - requires NVIDIA Container Toolkit
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8188/system_stats || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 60s

  # ---------------------------------------------------------------------------
  # ComfyUI CPU-only variant (uncomment if no GPU available)
  # ---------------------------------------------------------------------------
  # comfyui-cpu:
  #   image: frdel/comfyui-docker:latest
  #   container_name: ai-stack-comfyui-cpu
  #   ports:
  #     - "8188:8188"
  #   environment:
  #     - CLI_ARGS=--listen 0.0.0.0 --port 8188 --cpu
  #   volumes:
  #     - ./shared/comfyui/models:/comfyui/models
  #     - ./shared/comfyui/output:/comfyui/output
  #     - ./shared/comfyui/input:/comfyui/input
  #     - ./shared/comfyui/custom_nodes:/comfyui/custom_nodes
  #   networks:
  #     - ai-stack-network
  #   restart: unless-stopped
  #   profiles:
  #     - cpu-only

networks:
  ai-stack-network:
    driver: bridge
    name: ai-stack-network

volumes:
  n8n-data:
  agent-zero-data:
  comfyui-models:
  comfyui-output:
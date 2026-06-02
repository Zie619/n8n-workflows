# 🤖 AI Automation Stack

> **Turnkey Local AI Automation: n8n + Agent Zero + ComfyUI**

A single-command deployable stack for AI-powered workflow automation with image generation capabilities.

---

## 📚 Documentation

**👉 [START HERE: Documentation Index](INDEX.md)** - Choose the right guide for you!

- **🚀 [QUICK START](QUICK-START.md)** - 3 simple steps to get started
- **📖 [EASY INSTALL GUIDE](EASY-INSTALL.md)** - Step-by-step for Windows/Mac
- **🐧 [UBUNTU INSTALL GUIDE](UBUNTU-INSTALL.md)** - Complete guide for Ubuntu/Linux
- **🔧 [TROUBLESHOOTING](TROUBLESHOOTING.md)** - Fix common problems
- **📋 [SUMMARY](SUMMARY.md)** - Overview &amp; learning path
- **🎯 [CHEAT SHEET](CHEAT-SHEET.md)** - Quick reference (print this!)
- **📘 Full Documentation** - You're reading it now!

---

## 🎯 What's Included

| Service | Purpose | Port | URL |
|---------|---------|------|-----|
| **n8n** | Workflow automation engine (the conductor) | 5678 | http://localhost:5678 |
| **Agent Zero** | AI agent runtime & planning UI | 50080 | http://localhost:50080 |
| **ComfyUI** | AI image/video generation | 8188 | http://localhost:8188 |

---

## 🚀 Quick Start

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- (Optional) NVIDIA GPU with [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) for GPU acceleration

### One-Command Launch

**Windows (PowerShell):**
```powershell
.\start.ps1
```

**Linux/macOS:**
```bash
chmod +x start.sh
./start.sh
```

That's it! The script will:
1. ✅ Check Docker is installed and running
2. ✅ Detect GPU availability
3. ✅ Create all necessary directories
4. ✅ Pull the latest images
5. ✅ Start all services
6. ✅ Display access URLs

---

## 📁 Directory Structure

```
ai-stack/
├── docker-compose.yml      # Main stack configuration
├── .env                    # Environment variables
├── start.ps1               # Windows startup script
├── start.sh                # Linux/macOS startup script
├── README.md               # This file
│
├── data/                   # Persistent data (auto-created)
│   ├── n8n/                # n8n workflows & credentials
│   └── agent-zero/         # Agent Zero data
│
├── shared/                 # Shared between all services
│   ├── comfyui/
│   │   ├── models/         # AI models (checkpoints, LoRAs, etc.)
│   │   │   ├── checkpoints/
│   │   │   ├── loras/
│   │   │   ├── vae/
│   │   │   ├── controlnet/
│   │   │   └── embeddings/
│   │   ├── output/         # Generated images
│   │   ├── input/          # Input images
│   │   └── custom_nodes/   # ComfyUI extensions
│   └── workflows/          # Shared workflow files
│
└── workflows/              # Pre-built n8n workflows
    ├── comfyui-image-generation.json
    └── comfyui-simple-test.json
```

---

## 🔧 Commands

### Windows (PowerShell)

```powershell
.\start.ps1              # Start the stack
.\start.ps1 -Stop        # Stop the stack
.\start.ps1 -Logs        # View logs
.\start.ps1 -Status      # Check status
.\start.ps1 -NoPull      # Start without pulling images
.\start.ps1 -CPU         # Force CPU mode (no GPU)
```

### Linux/macOS

```bash
./start.sh               # Start the stack
./start.sh --stop        # Stop the stack
./start.sh --logs        # View logs
./start.sh --status      # Check status
./start.sh --no-pull     # Start without pulling images
./start.sh --cpu         # Force CPU mode (no GPU)
```

### Docker Compose (Direct)

```bash
docker compose up -d     # Start
docker compose down      # Stop
docker compose logs -f   # View logs
docker compose ps        # Status
```

---

## 🎨 Adding Models to ComfyUI

Place your models in the appropriate directories:

| Model Type | Directory |
|------------|-----------|
| Stable Diffusion checkpoints | `shared/comfyui/models/checkpoints/` |
| LoRA models | `shared/comfyui/models/loras/` |
| VAE models | `shared/comfyui/models/vae/` |
| ControlNet models | `shared/comfyui/models/controlnet/` |
| Upscale models | `shared/comfyui/models/upscale_models/` |
| Embeddings | `shared/comfyui/models/embeddings/` |

### Recommended Starter Model

Download [SD 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned-emaonly.safetensors) and place it in `shared/comfyui/models/checkpoints/`.

---

## 📊 Pre-built Workflows

### 1. ComfyUI Image Generation Pipeline

**File:** `workflows/comfyui-image-generation.json`

A complete webhook-triggered image generation pipeline:

1. Import the workflow into n8n
2. Activate the workflow
3. Send a POST request:

```bash
curl -X POST http://localhost:5678/webhook/generate-image \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "a cyberpunk city at night, neon lights, rain, highly detailed",
    "negative_prompt": "blurry, low quality",
    "steps": 20,
    "cfg": 7,
    "width": 512,
    "height": 512
  }'
```

### 2. ComfyUI Simple Test

**File:** `workflows/comfyui-simple-test.json`

A simple connectivity test:

1. Import and activate in n8n
2. Visit: http://localhost:5678/webhook/comfyui-status
3. Should return ComfyUI system stats

---

## 🔗 Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         n8n (Conductor)                         │
│                      http://localhost:5678                      │
└─────────────────────┬───────────────────────┬───────────────────┘
                      │                       │
                      ▼                       ▼
┌─────────────────────────────┐ ┌─────────────────────────────────┐
│       Agent Zero            │ │           ComfyUI               │
│   http://localhost:50080    │ │     http://localhost:8188       │
│                             │ │                                 │
│  • AI planning/reasoning    │ │  • POST /prompt (queue job)     │
│  • Tool use decisions       │ │  • GET /history/{id} (results)  │
│  • Prompt optimization      │ │  • GET /view (retrieve images)  │
└─────────────────────────────┘ └─────────────────────────────────┘
                      │                       │
                      └───────────┬───────────┘
                                  ▼
                    ┌─────────────────────────┐
                    │    Shared Volume        │
                    │      ./shared/          │
                    │                         │
                    │  • ComfyUI outputs      │
                    │  • Shared workflows     │
                    │  • Cross-service data   │
                    └─────────────────────────┘
```

### Typical Workflow Loop

1. **Trigger**: n8n receives webhook/schedule/event
2. **Plan** (optional): n8n calls Agent Zero for decision-making
3. **Generate**: n8n submits workflow to ComfyUI `POST /prompt`
4. **Poll**: n8n checks `GET /history/{prompt_id}` until complete
5. **Deliver**: n8n retrieves output and sends to destination

---

## 🌐 ComfyUI API Reference

### Queue a Generation

```bash
POST http://comfyui:8188/prompt
Content-Type: application/json

{
  "prompt": { /* ComfyUI workflow JSON */ }
}
```

**Response:**
```json
{
  "prompt_id": "abc123-def456-..."
}
```

### Check Status

```bash
GET http://comfyui:8188/history/{prompt_id}
```

### Get Queue Status

```bash
GET http://comfyui:8188/queue
```

### Retrieve Generated Image

```bash
GET http://comfyui:8188/view?filename={name}&subfolder=&type=output
```

### System Stats

```bash
GET http://comfyui:8188/system_stats
```

---

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Timezone
TZ=America/Los_Angeles

# n8n Basic Auth (optional)
N8N_BASIC_AUTH_ACTIVE=false
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=changeme

# API Keys for Agent Zero (optional)
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Custom Webhook URL

If running behind a reverse proxy:

```bash
WEBHOOK_URL=https://your-domain.com
```

---

## 🔒 Security Notes

- By default, all services are only accessible on localhost
- For production deployment, add a reverse proxy (Traefik/Caddy/nginx)
- Enable n8n basic auth for any non-local deployment
- Keep API keys in `.env` file (not committed to git)

---

## 🐛 Troubleshooting

### ComfyUI can't see GPU

1. Ensure NVIDIA drivers are installed
2. Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
3. Restart Docker Desktop
4. Run `docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi` to test

### Services won't start

```bash
# Check logs
docker compose logs -f

# Restart specific service
docker compose restart n8n

# Full reset
docker compose down -v
docker compose up -d
```

### n8n can't connect to ComfyUI

- Use `http://comfyui:8188` (Docker internal network), not `localhost`
- Ensure ComfyUI container is healthy: `docker compose ps`

### Port conflicts

Edit `docker-compose.yml` to change port mappings:
```yaml
ports:
  - "NEW_PORT:INTERNAL_PORT"
```

---

## 📚 Resources

- [n8n Documentation](https://docs.n8n.io/)
- [Agent Zero GitHub](https://github.com/frdel/agent-zero)
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI API Examples](https://github.com/comfyanonymous/ComfyUI/blob/master/script_examples/basic_api_example.py)

---

## 📄 License

MIT License - Use freely for personal and commercial projects.
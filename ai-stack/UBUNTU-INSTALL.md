# 🐧 Ubuntu Installation Guide
## AI Automation Stack for Ubuntu/Linux

---

## ✅ Step 1: Install Docker on Ubuntu

### Open Terminal
Press `Ctrl + Alt + T` to open Terminal

### Check if Docker is Already Installed
```bash
docker --version
```

If you see a version number, skip to Step 2. Otherwise, continue:

### Install Docker
Copy and paste these commands one at a time:

```bash
# Update package list
sudo apt update

# Install required packages
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package list again
sudo apt update

# Install Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add your user to docker group (so you don't need sudo)
sudo usermod -aG docker $USER

# Apply the new group membership
newgrp docker
```

### Verify Docker Installation
```bash
docker --version
docker compose version
```

You should see version numbers for both.

---

## 📥 Step 2: Download the AI Stack

### Option A: Using Git (Recommended)
```bash
# Install git if you don't have it
sudo apt install -y git

# Clone the repository
git clone https://github.com/insomniakin/n8n-workflows.git

# Go to the ai-stack folder
cd n8n-workflows/ai-stack
```

### Option B: Download ZIP
```bash
# Install wget and unzip if you don't have them
sudo apt install -y wget unzip

# Download the repository
wget https://github.com/insomniakin/n8n-workflows/archive/refs/heads/feature/ai-automation-stack.zip

# Unzip it
unzip feature/ai-automation-stack.zip

# Go to the ai-stack folder
cd n8n-workflows-feature-ai-automation-stack/ai-stack
```

---

## 🚀 Step 3: Start the AI Stack

### Make the Script Executable
```bash
chmod +x start.sh
```

### Run the Stack
```bash
./start.sh
```

### What You'll See
The script will:
1. ✓ Check Docker is installed
2. ✓ Check Docker is running
3. ✓ Detect your GPU (if you have NVIDIA)
4. ✓ Create necessary folders
5. ✓ Pull Docker images (this takes 5-10 minutes first time)
6. ✓ Start all services

### Wait for Success Message
```
🎉 AI Stack is running!
```

---

## 🌐 Step 4: Open the Services

Open your web browser (Firefox, Chrome, etc.) and go to:

### n8n (Workflow Automation)
```
http://localhost:5678
```

### Agent Zero (AI Assistant)
```
http://localhost:50080
```

### ComfyUI (Image Generation)
```
http://localhost:8188
```

---

## 🎮 Quick Commands

### Start the Stack
```bash
./start.sh
```

### Stop the Stack
```bash
./start.sh --stop
```

### Check Status
```bash
./start.sh --status
```

### View Logs
```bash
./start.sh --logs
```

### Force CPU Mode (No GPU)
```bash
./start.sh --cpu
```

---

## 🔧 Ubuntu-Specific Troubleshooting

### Problem: "Permission denied" when running docker

**Solution:**
```bash
# Add yourself to docker group
sudo usermod -aG docker $USER

# Log out and log back in, or run:
newgrp docker

# Try again
./start.sh
```

### Problem: "Cannot connect to Docker daemon"

**Solution:**
```bash
# Start Docker service
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Check status
sudo systemctl status docker
```

### Problem: Port already in use

**Solution:**
```bash
# Find what's using the port
sudo lsof -i :5678
sudo lsof -i :8188
sudo lsof -i :50080

# Kill the process (replace PID with actual number)
sudo kill -9 PID

# Or just restart
sudo reboot
```

### Problem: Not enough disk space

**Solution:**
```bash
# Check disk space
df -h

# Clean up Docker
docker system prune -a

# Clean up apt cache
sudo apt clean
sudo apt autoremove
```

### Problem: NVIDIA GPU not detected

**Solution:**
```bash
# Install NVIDIA drivers
sudo ubuntu-drivers autoinstall

# Install NVIDIA Container Toolkit
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt update
sudo apt install -y nvidia-container-toolkit

# Restart Docker
sudo systemctl restart docker

# Test GPU
docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

---

## 🔥 Firewall Configuration (Optional)

If you want to access from other computers on your network:

```bash
# Allow ports through firewall
sudo ufw allow 5678/tcp
sudo ufw allow 8188/tcp
sudo ufw allow 50080/tcp

# Enable firewall if not already enabled
sudo ufw enable

# Check status
sudo ufw status
```

---

## 📊 System Requirements

### Minimum (CPU Mode)
- Ubuntu 20.04 or newer
- 8 GB RAM
- 20 GB free disk space
- Any modern CPU

### Recommended (GPU Mode)
- Ubuntu 20.04 or newer
- 16 GB RAM
- 50 GB free disk space
- NVIDIA GPU with 6+ GB VRAM
- NVIDIA drivers installed

---

## 🆘 Quick Help Commands

### Check Docker Status
```bash
sudo systemctl status docker
```

### Check Running Containers
```bash
docker ps
```

### Check Docker Logs
```bash
docker compose logs -f
```

### Restart Everything
```bash
./start.sh --stop
docker system prune -f
./start.sh
```

### Complete Reset (Deletes All Data!)
```bash
./start.sh --stop
docker compose down -v
rm -rf data/ shared/
./start.sh
```

---

## 💡 Ubuntu Pro Tips

### 1. Create Desktop Shortcuts

Create a file `~/Desktop/ai-stack.desktop`:
```bash
cat > ~/Desktop/ai-stack.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=AI Stack
Comment=Start AI Automation Stack
Exec=gnome-terminal -- bash -c "cd ~/n8n-workflows/ai-stack && ./start.sh; exec bash"
Icon=applications-internet
Terminal=true
EOF

chmod +x ~/Desktop/ai-stack.desktop
```

### 2. Auto-Start on Boot

```bash
# Create systemd service
sudo nano /etc/systemd/system/ai-stack.service
```

Paste this:
```ini
[Unit]
Description=AI Automation Stack
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/YOUR_USERNAME/n8n-workflows/ai-stack
ExecStart=/home/YOUR_USERNAME/n8n-workflows/ai-stack/start.sh
ExecStop=/home/YOUR_USERNAME/n8n-workflows/ai-stack/start.sh --stop
User=YOUR_USERNAME

[Install]
WantedBy=multi-user.target
```

Replace `YOUR_USERNAME` with your actual username, then:
```bash
sudo systemctl enable ai-stack
sudo systemctl start ai-stack
```

### 3. Monitor Resources

```bash
# Install htop for better monitoring
sudo apt install -y htop

# Watch Docker stats
docker stats

# Watch GPU usage (if NVIDIA)
watch -n 1 nvidia-smi
```

---

## ✅ Success Checklist

- [ ] Docker installed and running
- [ ] Repository downloaded
- [ ] In the ai-stack folder
- [ ] start.sh is executable
- [ ] Script ran successfully
- [ ] All three URLs open in browser
- [ ] n8n shows welcome screen
- [ ] ComfyUI shows interface
- [ ] Agent Zero shows chat

---

## 🎉 You're All Set!

Your AI Automation Stack is now running on Ubuntu!

### Next Steps:
1. Import the test workflow: `workflows/comfyui-simple-test.json`
2. Try generating your first image
3. Read SUMMARY.md to learn more
4. Build your own workflows!

### Need More Help?
- **General Guide:** README.md
- **Troubleshooting:** TROUBLESHOOTING.md
- **Quick Reference:** CHEAT-SHEET.md

**Happy automating! 🚀**
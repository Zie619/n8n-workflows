# 🔧 Troubleshooting Guide

## Common Problems and How to Fix Them

---

## Problem 1: "Docker is not installed"

### What you see:
```
✗ Docker is not installed or not in PATH
```

### How to fix:
1. **Install Docker Desktop**
   - Windows: https://www.docker.com/products/docker-desktop
   - Mac: https://www.docker.com/products/docker-desktop
2. **Restart your computer**
3. **Try again**

---

## Problem 2: "Docker daemon is not running"

### What you see:
```
✗ Docker daemon is not running
```

### How to fix:
1. **Look for the Docker whale icon** 🐳
   - Windows: Bottom right corner (system tray)
   - Mac: Top right corner (menu bar)
2. **If you don't see it:**
   - Open "Docker Desktop" from your applications
   - Wait 30 seconds for it to start
3. **When you see the whale icon, try again**

---

## Problem 3: "Permission denied" (Mac only)

### What you see:
```
Permission denied
```

### How to fix:
1. **Open Terminal**
2. **Type these commands one at a time:**
   ```bash
   cd ~/Downloads/n8n-workflows-main/ai-stack
   chmod +x start.sh
   ./start.sh
   ```
3. **Press Enter after each line**

---

## Problem 4: "Port already in use"

### What you see:
```
Error: Port 5678 is already in use
```

### How to fix:

**Option 1 - Stop other programs:**
1. Close all web browsers
2. Close any other programs
3. Try again

**Option 2 - Restart computer:**
1. Restart your computer
2. Open Docker Desktop
3. Try again

**Option 3 - Stop the old stack:**

Windows:
```powershell
.\start.ps1 -Stop
```

Mac:
```bash
./start.sh --stop
```

Then start again.

---

## Problem 5: Script window closes immediately (Windows)

### What you see:
- PowerShell window opens and closes in 1 second
- You can't read any messages

### How to fix:
1. **Open PowerShell as Administrator:**
   - Click Windows Start button
   - Type "PowerShell"
   - Right-click "Windows PowerShell"
   - Click "Run as administrator"
   - Click "Yes" when asked

2. **Type this command:**
   ```powershell
   Set-ExecutionPolicy RemoteSigned
   ```
   Press Enter

3. **Type "Y" and press Enter**

4. **Now try running start.ps1 again**

---

## Problem 6: "Cannot connect to localhost:5678"

### What you see:
- Browser says "This site can't be reached"
- Or "Connection refused"

### How to fix:
1. **Wait 2 minutes** - services need time to start
2. **Check if Docker is running** (look for whale icon 🐳)
3. **Check if the stack is running:**
   
   Windows:
   ```powershell
   .\start.ps1 -Status
   ```
   
   Mac:
   ```bash
   ./start.sh --status
   ```

4. **Look for these services:**
   - ai-stack-n8n (should say "Up")
   - ai-stack-agent-zero (should say "Up")
   - ai-stack-comfyui (should say "Up")

5. **If any say "Exited" or "Error":**
   - Stop everything: `.\start.ps1 -Stop` or `./start.sh --stop`
   - Start again: `.\start.ps1` or `./start.sh`

---

## Problem 7: "No space left on device"

### What you see:
```
Error: No space left on device
```

### How to fix:
1. **Free up disk space:**
   - Delete old files you don't need
   - Empty your Recycle Bin / Trash
   - You need at least 10 GB free

2. **Clean Docker:**
   ```bash
   docker system prune -a
   ```
   Type "y" and press Enter when asked

3. **Try again**

---

## Problem 8: Downloads are very slow

### What you see:
- "Pulling images..." takes more than 30 minutes

### How to fix:
1. **Check your internet connection**
2. **Be patient** - first download is 5-10 GB
3. **Next time will be faster** (it remembers what it downloaded)

### Skip the download if you already have it:
Windows:
```powershell
.\start.ps1 -NoPull
```

Mac:
```bash
./start.sh --no-pull
```

---

## Problem 9: "GPU not detected" but I have a GPU

### What you see:
```
ℹ No NVIDIA GPU detected
```

### How to fix (NVIDIA GPUs only):

**Windows:**
1. Install NVIDIA drivers from: https://www.nvidia.com/download/index.aspx
2. Install NVIDIA Container Toolkit
3. Restart Docker Desktop
4. Try again

**Mac:**
- Mac doesn't support NVIDIA GPUs in Docker
- The stack will use CPU mode automatically
- It will be slower but still work

**Don't have NVIDIA GPU?**
- That's okay! Use CPU mode:
  
  Windows: `.\start.ps1 -CPU`
  
  Mac: `./start.sh --cpu`

---

## Problem 10: Everything looks fine but nothing works

### Try this "nuclear option":

**Windows:**
```powershell
# Stop everything
.\start.ps1 -Stop

# Remove all containers and data
docker compose down -v

# Start fresh
.\start.ps1
```

**Mac:**
```bash
# Stop everything
./start.sh --stop

# Remove all containers and data
docker compose down -v

# Start fresh
./start.sh
```

**⚠️ Warning:** This deletes all your data! You'll start completely fresh.

---

## Still Not Working?

### Check these basics:

- [ ] Is Docker Desktop installed?
- [ ] Is Docker Desktop running? (see whale icon 🐳)
- [ ] Do you have internet connection?
- [ ] Do you have at least 10 GB free disk space?
- [ ] Did you restart your computer after installing Docker?
- [ ] Are you in the correct folder (ai-stack)?

### Get the logs:

Windows:
```powershell
.\start.ps1 -Logs
```

Mac:
```bash
./start.sh --logs
```

**Take a screenshot of any red error messages and ask for help!**

---

## Quick Command Reference

| What you want | Windows | Mac |
|---------------|---------|-----|
| Start | `.\start.ps1` | `./start.sh` |
| Stop | `.\start.ps1 -Stop` | `./start.sh --stop` |
| Check status | `.\start.ps1 -Status` | `./start.sh --status` |
| View logs | `.\start.ps1 -Logs` | `./start.sh --logs` |
| CPU mode | `.\start.ps1 -CPU` | `./start.sh --cpu` |
| Skip download | `.\start.ps1 -NoPull` | `./start.sh --no-pull` |

---

## 📞 Getting Help

When asking for help, provide:

1. **Your operating system** (Windows 10, Windows 11, Mac, etc.)
2. **What you were trying to do**
3. **The exact error message** (take a screenshot)
4. **What you already tried**

This helps people help you faster! 🚀
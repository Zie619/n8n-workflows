# 🎮 Super Easy Install Guide
## AI Automation Stack - Step by Step

---

## 📋 What You Need Before Starting

### ✅ Step 1: Check if you have Docker

**Windows:**
1. Click the Windows Start button (bottom left corner)
2. Type "Docker Desktop"
3. Do you see "Docker Desktop" in the list?
   - ✅ **YES** → Go to Step 2
   - ❌ **NO** → Go to "Installing Docker" section below

**Mac:**
1. Click the magnifying glass (🔍) in top right corner
2. Type "Docker"
3. Do you see "Docker" in the list?
   - ✅ **YES** → Go to Step 2
   - ❌ **NO** → Go to "Installing Docker" section below

---

## 🔽 Installing Docker (If You Don't Have It)

### For Windows:

1. **Open your web browser** (Chrome, Edge, Firefox)
2. **Go to this website:** https://www.docker.com/products/docker-desktop
3. **Click the big blue button** that says "Download for Windows"
4. **Wait for the download** (it's a big file, might take 5-10 minutes)
5. **Find the downloaded file** (usually in your Downloads folder)
6. **Double-click the file** to install
7. **Click "Yes"** when Windows asks if you want to install
8. **Follow the installer** - just keep clicking "Next" and "OK"
9. **Restart your computer** when it asks
10. **After restart**, Docker Desktop will open automatically

### For Mac:

1. **Open your web browser** (Safari, Chrome, Firefox)
2. **Go to this website:** https://www.docker.com/products/docker-desktop
3. **Click the big blue button** that says "Download for Mac"
4. **Wait for the download** (it's a big file, might take 5-10 minutes)
5. **Find the downloaded file** (usually in your Downloads folder)
6. **Double-click the file** to open it
7. **Drag the Docker icon** into the Applications folder
8. **Open Applications folder** and double-click Docker
9. **Click "Open"** when Mac asks if you're sure
10. **Wait for Docker to start** (you'll see a whale icon in the top menu bar)

---

## 📥 Step 2: Download the AI Stack

### Windows:

1. **Open your web browser**
2. **Go to:** https://github.com/insomniakin/n8n-workflows
3. **Click the green "Code" button**
4. **Click "Download ZIP"**
5. **Wait for download to finish**
6. **Go to your Downloads folder**
7. **Right-click the ZIP file**
8. **Click "Extract All"**
9. **Click "Extract"**
10. **Open the extracted folder**
11. **Find the folder called "ai-stack"**
12. **Remember where this folder is!**

### Mac:

1. **Open your web browser**
2. **Go to:** https://github.com/insomniakin/n8n-workflows
3. **Click the green "Code" button**
4. **Click "Download ZIP"**
5. **Wait for download to finish**
6. **Go to your Downloads folder**
7. **Double-click the ZIP file** (it extracts automatically)
8. **Open the extracted folder**
9. **Find the folder called "ai-stack"**
10. **Remember where this folder is!**

---

## 🚀 Step 3: Start the AI Stack

### Windows:

1. **Open File Explorer** (the folder icon on your taskbar)
2. **Go to the "ai-stack" folder** you found in Step 2
3. **Find the file called "start.ps1"**
4. **Right-click on "start.ps1"**
5. **Click "Run with PowerShell"**
6. **If Windows asks "Do you want to allow this?"** → Click "Yes"
7. **Wait and watch the window** - you'll see lots of text scrolling
8. **Look for these messages:**
   ```
   ✓ Docker found
   ✓ Docker daemon is running
   ✓ All images pulled successfully
   🎉 AI Stack is running!
   ```
9. **When you see "AI Stack is running!" → You're done!**

### Mac:

1. **Open Finder**
2. **Go to the "ai-stack" folder** you found in Step 2
3. **Right-click (or Control+click) on "start.sh"**
4. **Click "Open With" → "Terminal"**
5. **If Mac says "Permission denied":**
   - Type: `chmod +x start.sh`
   - Press Enter
   - Type: `./start.sh`
   - Press Enter
6. **Wait and watch the window** - you'll see lots of text scrolling
7. **Look for these messages:**
   ```
   ✓ Docker found
   ✓ Docker daemon is running
   ✓ All images pulled successfully
   🎉 AI Stack is running!
   ```
8. **When you see "AI Stack is running!" → You're done!**

---

## 🌐 Step 4: Open the Programs

Now you can use the AI tools! Open your web browser and go to these addresses:

### 1. n8n (Workflow Maker)
- **Type this in your browser:** `http://localhost:5678`
- **Press Enter**
- **You should see:** A welcome screen asking you to create an account
- **Create an account** with any email and password (it's only on your computer)

### 2. Agent Zero (AI Helper)
- **Type this in your browser:** `http://localhost:50080`
- **Press Enter**
- **You should see:** A chat interface

### 3. ComfyUI (Image Maker)
- **Type this in your browser:** `http://localhost:8188`
- **Press Enter**
- **You should see:** A node-based interface for making images

---

## ❓ Troubleshooting (If Something Goes Wrong)

### Problem: "Docker is not running"

**Solution:**
1. Look for the Docker icon (a whale) in your taskbar (Windows) or menu bar (Mac)
2. If you don't see it, open Docker Desktop
3. Wait until you see "Docker Desktop is running"
4. Try running the start script again

### Problem: "Port already in use"

**Solution:**
1. Close any programs that might be using the internet
2. Restart your computer
3. Try again

### Problem: The script window closes immediately

**Windows Solution:**
1. Open PowerShell as Administrator:
   - Click Start
   - Type "PowerShell"
   - Right-click "Windows PowerShell"
   - Click "Run as administrator"
2. Type: `Set-ExecutionPolicy RemoteSigned`
3. Press Enter
4. Type "Y" and press Enter
5. Try running start.ps1 again

### Problem: "Cannot find Docker"

**Solution:**
1. Make sure you installed Docker Desktop (see "Installing Docker" section)
2. Make sure Docker Desktop is open and running
3. Restart your computer
4. Try again

---

## 🛑 How to Stop the AI Stack

### Windows:
1. Open PowerShell (same way as before)
2. Go to the ai-stack folder:
   - Type: `cd ` (with a space after cd)
   - Drag the ai-stack folder into the PowerShell window
   - Press Enter
3. Type: `.\start.ps1 -Stop`
4. Press Enter

### Mac:
1. Open Terminal
2. Go to the ai-stack folder:
   - Type: `cd ` (with a space after cd)
   - Drag the ai-stack folder into the Terminal window
   - Press Enter
3. Type: `./start.sh --stop`
4. Press Enter

---

## 📞 Need More Help?

If you're still stuck:

1. **Take a screenshot** of any error messages
2. **Write down exactly what step you're on**
3. **Ask someone for help** and show them:
   - This guide
   - Your screenshot
   - What step you're stuck on

---

## ✅ Quick Checklist

Before you start, make sure:
- [ ] Docker Desktop is installed
- [ ] Docker Desktop is running (you can see the whale icon)
- [ ] You downloaded the ai-stack folder
- [ ] You know where the ai-stack folder is on your computer
- [ ] Your internet is working

---

## 🎉 Success! What Now?

Once everything is running, you can:

1. **Learn n8n:** Go to http://localhost:5678 and try making a simple workflow
2. **Talk to Agent Zero:** Go to http://localhost:50080 and ask it questions
3. **Make images:** Go to http://localhost:8188 and try generating an image

**Have fun! 🚀**
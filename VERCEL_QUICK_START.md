# ⚡ Vercel Deployment - Quick Start

## 🎯 **3-Minute Deployment**

### **Step 1: Import Project (30 seconds)**
1. Go to: https://vercel.com/new
2. Click "Import Git Repository"
3. Select: `adarshnayik/deepfake-detector`
4. Click "Import"

### **Step 2: Generate SECRET_KEY (30 seconds)**
Run this command locally:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy the output (you'll need it in Step 3)

### **Step 3: Add Environment Variables (1 minute)**
In Vercel UI, add these environment variables:

```
SECRET_KEY=<paste-the-key-from-step-2>
UPLOAD_FOLDER=/tmp/uploads
MODEL_PATH=models/deepfake_detector.h5
```

### **Step 4: Deploy (1 minute)**
Click **"Deploy"** button and wait!

---

## ✅ **That's It!**

Your app will be live at: `https://your-project.vercel.app`

Build time: 2-4 minutes (normal for TensorFlow)

---

## 📋 **Configuration Summary**

| Setting | Value |
|---------|-------|
| **Framework** | Other |
| **Root Directory** | `./` |
| **Build Command** | (auto-detected) |
| **Output Directory** | (auto-detected) |
| **Python Version** | 3.11.0 (from runtime.txt) |

---

## 🔑 **Environment Variables**

### **Required:**
- `SECRET_KEY` - Generate with Python command above
- `UPLOAD_FOLDER` - Set to `/tmp/uploads`

### **Optional:**
- `MODEL_PATH` - Set to `models/deepfake_detector.h5`

---

## ⏱️ **Expected Times**

- **Build:** 2-4 minutes ✅
- **First Request:** 10-20 seconds (cold start) ✅
- **Subsequent Requests:** 1-2 seconds ✅

---

## 🚨 **Common Issues**

### **"pip: command not found"**
✅ **Fixed!** The new configuration uses `@vercel/python` builder

### **"Model not found"**
✅ **Expected!** App runs in demo mode without model file

### **"Deployment taking too long"**
✅ **Normal!** TensorFlow is large (~500MB), first build takes time

---

## 📖 **Full Documentation**

For detailed instructions, see: `VERCEL_DEPLOYMENT_GUIDE.md`

---

## 🎉 **Ready to Deploy!**

All configuration files are ready in your repository:
- ✅ `vercel.json`
- ✅ `runtime.txt`
- ✅ `requirements.txt`
- ✅ `api/index.py`

Just follow the 4 steps above and you're done! 🚀

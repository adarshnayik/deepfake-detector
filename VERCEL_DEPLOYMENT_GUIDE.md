# 🚀 Vercel Deployment Guide - AI Deepfake Detector

## ✅ **Configuration Files Ready**

Your repository now has the correct configuration files for Vercel deployment:

1. ✅ `vercel.json` - Vercel configuration
2. ✅ `runtime.txt` - Python version specification
3. ✅ `requirements.txt` - Python dependencies
4. ✅ `api/index.py` - Main Flask application

---

## 📋 **Step-by-Step Deployment Instructions**

### **Method 1: Import from GitHub (Recommended)**

#### **Step 1: Go to Vercel Dashboard**
Visit: https://vercel.com/new

#### **Step 2: Import Your Repository**
1. Click **"Import Git Repository"**
2. Select: `adarshnayik/deepfake-detector`
3. Click **"Import"**

#### **Step 3: Configure Project Settings**

**Framework Preset:** `Other` (leave as default)

**Root Directory:** `./` (leave as default)

**Build Command:** Leave empty (Vercel will auto-detect from vercel.json)

**Output Directory:** Leave empty

**Install Command:** Leave empty

#### **Step 4: Add Environment Variables**

Click **"Environment Variables"** and add these:

| Variable Name | Value | Required |
|--------------|-------|----------|
| `SECRET_KEY` | `your-secret-key-here` | ✅ Yes |
| `UPLOAD_FOLDER` | `/tmp/uploads` | ✅ Yes |
| `MODEL_PATH` | `models/deepfake_detector.h5` | ⚠️ Optional |

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it as your `SECRET_KEY` value.

#### **Step 5: Deploy**
1. Click **"Deploy"** button
2. Wait 2-4 minutes for build to complete
3. Your app will be live at: `https://your-project.vercel.app`

---

## 🔧 **Configuration Details**

### **vercel.json**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index"
    }
  ],
  "env": {
    "FLASK_ENV": "production",
    "FLASK_APP": "api/index.py"
  }
}
```

### **runtime.txt**
```
python-3.11.0
```

### **requirements.txt**
All dependencies are already specified in your `requirements.txt` file.

---

## ⚙️ **Environment Variables Explained**

### **Required Variables:**

1. **SECRET_KEY**
   - Purpose: Flask session security
   - Generate with: `python -c "import secrets; print(secrets.token_hex(32))"`
   - Example: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6`

2. **UPLOAD_FOLDER**
   - Purpose: Temporary file storage
   - Value: `/tmp/uploads`
   - Note: Vercel only allows writes to `/tmp` directory

### **Optional Variables:**

3. **MODEL_PATH**
   - Purpose: Path to TensorFlow model file
   - Value: `models/deepfake_detector.h5`
   - Note: If model file doesn't exist, app runs in demo mode

---

## 🚨 **Common Issues & Solutions**

### **Issue 1: Build Command Error**
**Error:** `pip: command not found`

**Solution:** 
- ✅ Already fixed! The new `vercel.json` uses `@vercel/python` builder
- ✅ `runtime.txt` specifies Python 3.11.0
- No manual build command needed

### **Issue 2: Module Not Found**
**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
- Ensure `requirements.txt` is in the root directory
- Vercel automatically installs dependencies from `requirements.txt`

### **Issue 3: Model File Not Found**
**Error:** `Model file not found`

**Solution:**
- This is expected! The app runs in **demo mode** without the model
- Demo mode uses simulated predictions
- To use real model: Upload model file to external storage (AWS S3, Google Cloud Storage)

### **Issue 4: Deployment Takes Too Long**
**Expected Times:**
- ✅ Build: 2-4 minutes (normal for TensorFlow)
- ✅ First request: 10-20 seconds (cold start)
- ✅ Subsequent requests: 1-2 seconds

**Why it's slow:**
- TensorFlow is a large library (~500MB)
- First deployment downloads and caches dependencies
- Subsequent deployments are faster

### **Issue 5: Function Timeout**
**Error:** `Function execution timed out`

**Solution:**
- Free tier: 10 second timeout
- Pro tier: 60 second timeout
- Training features won't work on Vercel (use local or cloud VM)
- Image analysis should complete within timeout

---

## 📊 **What Works on Vercel**

✅ **Working Features:**
- Image upload and analysis
- Deepfake detection (demo mode)
- Image editing detection
- Statistics dashboard
- All static pages (About, Contact, etc.)
- API endpoints

⚠️ **Limited Features:**
- Model training (requires long-running process)
- Large file uploads (10MB limit)
- Persistent file storage (use external storage)

---

## 🎯 **Post-Deployment Steps**

### **1. Test Your Deployment**

Visit your deployment URL and test:
- ✅ Homepage loads
- ✅ Upload an image
- ✅ Check analysis results
- ✅ Navigate to different pages

### **2. Configure Custom Domain (Optional)**

1. Go to Project Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed
4. Wait for SSL certificate (automatic)

### **3. Enable Auto-Deploy**

Vercel automatically deploys on every push to `main` branch:
- ✅ Already configured!
- Every `git push` triggers a new deployment
- Preview deployments for pull requests

### **4. Monitor Performance**

Check Vercel Dashboard for:
- Function execution time
- Error logs
- Bandwidth usage
- Request count

---

## 🔄 **Updating Your Deployment**

To update your deployed app:

```bash
# Make changes to your code
git add .
git commit -m "Your update message"
git push origin main
```

Vercel will automatically:
1. Detect the push
2. Build the new version
3. Deploy to production
4. Keep the same URL

---

## 🆘 **Need Help?**

### **Check Deployment Logs:**
1. Go to Vercel Dashboard
2. Select your project
3. Click on the deployment
4. View "Build Logs" and "Function Logs"

### **Common Log Messages:**

**✅ Success:**
```
✓ Build completed successfully
✓ Deployment ready
```

**⚠️ Warning (OK to ignore):**
```
Warning: TensorFlow not available - running without model inference
Warning: Running in demo mode
```

**❌ Error (needs fixing):**
```
Error: Module not found
Error: Build failed
```

---

## 📝 **Quick Copy-Paste Configuration**

### **For Vercel UI:**

**Environment Variables:**
```
SECRET_KEY=<generate-with-python-command>
UPLOAD_FOLDER=/tmp/uploads
MODEL_PATH=models/deepfake_detector.h5
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## ✅ **Deployment Checklist**

Before deploying, ensure:

- [x] `vercel.json` exists in root directory
- [x] `runtime.txt` exists in root directory
- [x] `requirements.txt` exists in root directory
- [x] `api/index.py` exists
- [x] All changes committed and pushed to GitHub
- [ ] SECRET_KEY generated
- [ ] Environment variables configured in Vercel
- [ ] Project imported in Vercel
- [ ] Deployment initiated

---

## 🎉 **Expected Result**

After successful deployment:

1. ✅ Your app is live at: `https://your-project.vercel.app`
2. ✅ Auto-deploy enabled for future updates
3. ✅ HTTPS enabled automatically
4. ✅ CDN for static files
5. ✅ Preview URLs for pull requests

---

## 📞 **Support Resources**

- **Vercel Documentation:** https://vercel.com/docs
- **Python on Vercel:** https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **GitHub Repository:** https://github.com/adarshnayik/deepfake-detector

---

## 🚀 **Ready to Deploy!**

Your repository is now properly configured for Vercel deployment. Follow the steps above to deploy your AI Deepfake Detector to production!

**Good luck! 🎉**

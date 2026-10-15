Live Model - https://deepfake-detector-ai.vercel.app/
# 🧠 AI Deepfake Detection Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)](https://flask.palletsprojects.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black.svg)](https://vercel.com)

> **Advanced AI-powered platform for detecting deepfake images with real-time training capabilities and comprehensive analytics.**

![Deepfake Detector](deepfake-detector.png)

---

## 🌟 Key Features

### 🎯 **Core Detection**
- **Multi-Model Support**: Train and deploy custom CNN models
- **Real-time Analysis**: Instant deepfake detection with confidence scores
- **Batch Processing**: Analyze multiple images simultaneously
- **Advanced Metrics**: Precision, recall, F1-score, and accuracy tracking

### 🚀 **Training System**
- **Interactive Training Interface**: Real-time progress monitoring
- **Live Metrics Dashboard**: Training/validation loss and accuracy graphs
- **Epoch-by-Epoch Tracking**: Detailed performance visualization
- **Model Checkpointing**: Automatic saving of best models
- **Training Logs**: Comprehensive training history and analytics

### 📊 **Analytics & Visualization**
- **Real-time Statistics**: Live performance metrics and system health
- **Interactive Charts**: Beautiful Chart.js visualizations
- **Training History**: Complete training session analytics
- **Model Comparison**: Compare different model performances
- **Detection Gallery**: Browse analyzed images with results

### 🎨 **Modern UI/UX**
- **Responsive Design**: Mobile-first, works on all devices
- **Dark/Light Themes**: Customizable interface themes
- **Drag & Drop Upload**: Intuitive file upload experience
- **Real-time Updates**: Live progress bars and notifications
- **Professional Dashboard**: Clean, modern interface design

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 4GB+ RAM recommended
- Modern web browser

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/adarshnayik/deepfake-detector.git
cd deepfake-detector
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python run.py
```

The application will start at `http://localhost:5000`

**Alternative run methods:**
```bash
# Using Flask directly
python api/index.py

# Using Flask CLI
flask --app api.index run
```

---

## 📱 Usage Guide

### 1. **Image Detection**
- Navigate to the home page
- Drag & drop an image or click to browse
- Select detection model (if multiple available)
- View instant results with confidence scores
- See detailed analysis metrics

### 2. **Model Training**
- Go to the Training page
- Configure training parameters:
  - Number of epochs
  - Batch size
  - Learning rate
  - Model architecture
- Start training and monitor:
  - Real-time loss/accuracy graphs
  - Epoch progress bars
  - Training logs
  - Validation metrics
- Download trained model when complete

### 3. **Analytics Dashboard**
- View comprehensive statistics
- Analyze detection history
- Compare model performances
- Monitor system health
- Export analytics data

### 4. **Gallery**
- Browse detection examples
- Filter by categories
- View detailed analysis results
- Learn from real cases

---

## 🏗️ Project Structure

```
deepfake-detector/
├── api/
│   └── index.py              # Main Flask application
├── templates/
│   ├── index.html            # Home/Detection page
│   ├── training.html         # Training interface
│   ├── statistics.html       # Analytics dashboard
│   ├── about.html            # About page
│   └── contact.html          # Contact page
├── static/
│   ├── training-manager.js   # Training logic
│   ├── chatbot.js            # AI assistant
│   ├── theme-manager.js      # Theme switching
│   └── gallery/              # Detection examples
├── models/                   # Trained model files
├── datasets/                 # Training datasets
├── checkpoints/              # Model checkpoints
├── logs/                     # Training logs
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment config
└── run.py                   # Application launcher
```

---

## 🔧 API Endpoints

### Detection
```bash
POST /api/upload              # Upload and analyze image
GET  /api/models              # Get available models
GET  /api/statistics          # Get system statistics
```

### Training
```bash
POST /api/train/start         # Start model training
GET  /api/train/status        # Get training status
GET  /api/train/logs          # Get training logs
POST /api/train/stop          # Stop training
```

### Utilities
```bash
POST /api/chatbot             # AI assistant chat
GET  /api/health              # System health check
```

---

## 🚀 Deployment

### Vercel (Recommended)

**Quick Deploy:**
1. Push code to GitHub
2. Import repository on [vercel.com](https://vercel.com)
3. Click "Deploy"

**CLI Deploy:**
```bash
# Install Vercel CLI
npm i -g vercel

# Login and deploy
vercel login
vercel --prod
```

📖 **Detailed Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md)

### Local Production
```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api.index:app

# Using Waitress (Windows)
pip install waitress
waitress-serve --port=5000 api.index:app
```

---

## 📊 Model Architecture

### Default CNN Model
```
Input (224x224x3)
    ↓
Conv2D (32 filters) → ReLU → MaxPool
    ↓
Conv2D (64 filters) → ReLU → MaxPool
    ↓
Conv2D (128 filters) → ReLU → MaxPool
    ↓
Flatten → Dense (128) → Dropout (0.5)
    ↓
Output (2 classes: Real/Fake)
```

### Training Features
- **Optimizer**: Adam with configurable learning rate
- **Loss Function**: Binary crossentropy
- **Metrics**: Accuracy, precision, recall, F1-score
- **Callbacks**: ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
- **Data Augmentation**: Rotation, flip, zoom, shift

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | 88.3% |
| **Precision** | 89.1% |
| **Recall** | 87.5% |
| **F1-Score** | 88.3% |
| **Inference Time** | ~0.2s per image |

*Note: Metrics vary based on trained model and dataset*

---

## 🛠️ Development

### Setup Development Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run in debug mode
python run.py
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=api tests/
```

---

## 📚 Documentation

- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment guide for Vercel/Railway
- **[DEPLOYMENT_STATUS.md](DEPLOYMENT_STATUS.md)** - Current deployment status
- **[GITHUB_PUSH_RESOLUTION.md](GITHUB_PUSH_RESOLUTION.md)** - Git optimization guide
- **[HOW_TO_RUN.md](HOW_TO_RUN.md)** - Detailed running instructions

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Project Team

- Adarsh
- Anil
- Kiran

- **Email**: adarshnayik2@gmail.com
- **Phone**: +91 9900893665
- **GitHub**: [@adarshnayik](https://github.com/adarshnayik)

---

## 🙏 Acknowledgments

- **TensorFlow** - Deep learning framework
- **Flask** - Web framework
- **Bootstrap** - UI framework
- **Chart.js** - Data visualization
- **Vercel** - Deployment platform
- All contributors and researchers in deepfake detection

---

## 📊 Repository Stats

![Repository Size](https://img.shields.io/github/repo-size/adarshnayik/deepfake-detector)
![Last Commit](https://img.shields.io/github/last-commit/adarshnayik/deepfake-detector)
![Issues](https://img.shields.io/github/issues/adarshnayik/deepfake-detector)
![Pull Requests](https://img.shields.io/github/issues-pr/adarshnayik/deepfake-detector)

---

## 🔮 Roadmap

- [ ] Video deepfake detection
- [ ] Real-time webcam analysis
- [ ] Multi-language support
- [ ] Mobile app (React Native)
- [ ] API rate limiting and authentication
- [ ] Advanced model architectures (EfficientNet, Vision Transformer)
- [ ] Explainable AI visualizations
- [ ] Batch API for enterprise use

---

## ⚠️ Disclaimer

This tool is for educational and research purposes. While it provides deepfake detection capabilities, no system is 100% accurate. Always verify critical information through multiple sources.

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by Adarsh, Anil, and Kiran

[Report Bug](https://github.com/adarshnayik/deepfake-detector/issues) · [Request Feature](https://github.com/adarshnayik/deepfake-detector/issues) · [Documentation](https://github.com/adarshnayik/deepfake-detector/wiki)

</div>

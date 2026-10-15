#!/usr/bin/env python
"""Check if all required dependencies are installed"""

import sys
print(f"Python Version: {sys.version}\n")
print("=" * 60)
print("Checking Required Dependencies")
print("=" * 60 + "\n")

required_packages = {
    'flask': 'Flask',
    'flask_cors': 'Flask-CORS',
    'PIL': 'Pillow',
    'numpy': 'NumPy',
    'werkzeug': 'Werkzeug',
    'requests': 'Requests',
    'cv2': 'OpenCV',
    'tensorflow': 'TensorFlow',
    'matplotlib': 'Matplotlib',
    'sklearn': 'Scikit-learn'
}

installed = []
missing = []

for pkg, display_name in required_packages.items():
    try:
        mod = __import__(pkg)
        version = getattr(mod, '__version__', 'unknown')
        print(f"✅ {display_name:20s} - {version}")
        installed.append(display_name)
    except ImportError:
        print(f"❌ {display_name:20s} - NOT INSTALLED")
        missing.append(display_name)

print("\n" + "=" * 60)
print(f"Summary: {len(installed)}/{len(required_packages)} packages installed")
print("=" * 60)

if missing:
    print(f"\n⚠️  Missing packages: {', '.join(missing)}")
    print("\nRun: pip install -r requirements-full.txt")
else:
    print("\n✅ All required packages are installed!")

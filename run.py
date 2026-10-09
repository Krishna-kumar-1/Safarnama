#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Safarnama - Universal Cross-Platform Launcher (Windows, Linux, macOS)
Usage:
    python run.py
"""

import os
import sys
import shutil
import subprocess
import webbrowser
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def ensure_env():
    env_file = ROOT / ".env"
    example_file = ROOT / ".env.example"
    if not env_file.exists() and example_file.exists():
        print("ℹ️  Creating .env configuration file from .env.example...")
        shutil.copy(example_file, env_file)
        print("💡 Tip: You can configure your Gemini and RailKit API keys in .env")

def ensure_dependencies():
    missing = []
    for pkg in ["flask", "networkx", "flask_cors", "cryptography"]:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"📦 Installing missing dependencies ({', '.join(missing)})...")
        req_file = ROOT / "requirements.txt"
        cmd = [sys.executable, "-m", "pip", "install", "-r", str(req_file)]
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print("❌ Failed to install dependencies. Please run: pip install -r requirements.txt")
            sys.exit(1)
        print("✔ Dependencies successfully installed!")

def open_browser():
    time.sleep(1.8)
    try:
        webbrowser.open("http://localhost:5000/journey")
    except Exception:
        pass

def main():
    print("=" * 60)
    print("  🚆 Safarnama: Indian Railways Route Finder & Train-Dhundho Live")
    print("=" * 60)
    print(f"Python: {sys.version.split()[0]} on {sys.platform}")

    ensure_env()
    ensure_dependencies()

    print("\n🚀 Starting server...")
    print("   • Landing Portal : http://localhost:5000/journey")
    print("   • Route Planner  : http://localhost:5000")
    print("   • Train-Dhundho  : http://localhost:5000/live")
    print("\nPress Ctrl+C to stop.\n")

    threading.Thread(target=open_browser, daemon=True).start()

    # Import and run app directly in current process
    sys.path.insert(0, str(ROOT))
    from app import app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# ==============================================================================
# Indian Railways Route Finder & NTES Live Cloud Portal ("Safarnama")
# Direct Launch Script for Linux & macOS
# ==============================================================================

set -e

# Change to script directory
cd "$(dirname "$0")"

echo "========================================================"
echo "  🚆 Safarnama - Starting Indian Railways Portal"
echo "========================================================"
echo ""

# 1. Check Python 3
if command -v python3 >/dev/null 2>&1; then
    PY_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PY_BIN="python"
else
    echo "❌ ERROR: Python 3 was not found on your system."
    echo "Please install Python 3.10+:"
    echo "  - Linux (Debian/Ubuntu): sudo apt update && sudo apt install python3 python3-pip python3-venv"
    echo "  - macOS: brew install python"
    echo ""
    exit 1
fi

echo "✔ Python detected: $($PY_BIN --version)"

# 2. Check Node.js (Optional for RailKit bridge, offline timetable still works without it)
if command -v node >/dev/null 2>&1; then
    echo "✔ Node.js detected: $(node --version)"
else
    echo "⚠️  Node.js not detected (optional for RailKit live satellite bridge)."
fi

# 3. Create .env from template if missing
if [ ! -f .env ] && [ -f .env.example ]; then
    echo "ℹ️  First time setup: creating .env from .env.example..."
    cp .env.example .env
    echo "💡 You can add your Gemini and RailKit API keys in .env at any time."
fi

# 4. Check & Install Python Dependencies
echo "📦 Checking Python dependencies..."
if ! $PY_BIN -c "import flask, networkx, flask_cors, cryptography" >/dev/null 2>&1; then
    echo "First run - installing required packages from requirements.txt..."
    $PY_BIN -m pip install -r requirements.txt
    echo "✔ Dependencies installed successfully."
fi

echo ""
echo "🚀 Server is starting on http://localhost:5000"
echo "   - Route Planner : http://localhost:5000"
echo "   - NTES Live     : http://localhost:5000/live"
echo "   - Overview      : http://localhost:5000/journey"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""

# 5. Open browser if desktop environment is present
if [ -n "$DISPLAY" ] || [ -n "$WAYLAND_DISPLAY" ] || [ "$(uname)" = "Darwin" ]; then
    (
        sleep 2
        if command -v xdg-open >/dev/null 2>&1; then
            xdg-open "http://localhost:5000/journey" >/dev/null 2>&1 || true
        elif command -v open >/dev/null 2>&1; then
            open "http://localhost:5000/journey" >/dev/null 2>&1 || true
        fi
    ) &
fi

# 6. Run Application
exec $PY_BIN app.py

@echo off
REM Double-click this file to start the Route Finder web app.
REM Keep this window OPEN while using the site. Closing it stops the server.

cd /d "%~dp0"

echo ============================================
echo   Route Finder - starting local server
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python was not found.
    echo Install it from https://python.org and tick "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

REM Copy .env.example if .env does not exist yet
if not exist .env (
    if exist .env.example (
        echo [INFO] First time setup: creating .env from .env.example...
        copy .env.example .env >nul
        echo [INFO] Created .env file. You can add your Gemini and RailKit API keys in it.
        echo.
    )
)

REM Check Node.js (Optional for RailKit bridge)
node --version >nul 2>&1
if errorlevel 1 (
    echo [NOTICE] Node.js not detected. Core graph routing and timetable works 100%% offline;
    echo          install Node.js 18+ to enable live satellite RailKit bridge if desired.
    echo.
)

REM Install anything missing; harmless if already present.
python -c "import flask, networkx, flask_cors" >nul 2>&1
if errorlevel 1 (
    echo First run - installing dependencies, please wait...
    python -m pip install -r requirements.txt
    echo.
)

echo Server starting...
echo.
echo   Landing page : http://localhost:5000/journey
echo   Route planner: http://localhost:5000
echo.
echo Opening your browser. KEEP THIS WINDOW OPEN.
echo Press Ctrl+C here (or close this window) to stop the server.
echo.

REM Give Flask a moment to bind the port before the browser opens.
start "" /b cmd /c "timeout /t 3 >nul && start http://localhost:5000/journey"

python app.py

echo.
echo Server stopped.
pause

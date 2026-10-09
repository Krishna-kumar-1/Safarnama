@echo off
setlocal EnableDelayedExpansion

REM ==============================================================================
REM   Safarnama - Indian Railways Route Finder and Train-Dhundho Live Portal
REM   All-in-One Windows Launcher: Auto-Installs Dependencies and Launches Server
REM   Double-click this file to run the web app.
REM   Keep this window OPEN while using the site. Closing it stops the server.
REM ==============================================================================

cd /d "%~dp0"
title Safarnama - Indian Railways and Train-Dhundho Portal

echo ==============================================================================
echo   Safarnama: Indian Railways Route Finder and Train-Dhundho Live Portal
echo ==============================================================================
echo.

REM 1. Unblock downloaded files if restricted by Windows Smart App Control
powershell -NoProfile -Command "Get-ChildItem -Path '%~dp0' -Recurse | Unblock-File -ErrorAction SilentlyContinue" >nul 2>&1

REM 2. Check Python installation (detects python, py launcher, or python3)
set "PY_CMD=python"
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if not errorlevel 1 (
        set "PY_CMD=py"
    ) else (
        python3 --version >nul 2>&1
        if not errorlevel 1 (
            set "PY_CMD=python3"
        ) else (
            echo [ERROR] Python was not found on your system!
            echo.
            echo Please install Python 3.10+ from:
            echo   https://www.python.org/downloads/
            echo.
            echo IMPORTANT: During installation, tick the box:
            echo   "[X] Add Python to PATH"
            echo.
            pause
            exit /b 1
        )
    )
)

echo [OK] Python detected:
%PY_CMD% --version
echo.

REM 3. Create .env from template if missing
if not exist "%~dp0.env" (
    if exist "%~dp0.env.example" (
        echo [INFO] First time setup: creating .env configuration file...
        copy "%~dp0.env.example" "%~dp0.env" >nul
        echo [OK] Created .env file.
        echo.
    )
)

REM 4. Check and Auto-Install Missing Dependencies
%PY_CMD% -c "import flask, networkx, flask_cors, cryptography" >nul 2>&1
if errorlevel 1 (
    echo [1/2] Installing required dependencies - first-time setup, please wait...
    echo.
    %PY_CMD% -m pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo.
        echo Retrying installation with user privileges...
        %PY_CMD% -m pip install --user -r "%~dp0requirements.txt"
        if errorlevel 1 (
            echo.
            echo [ERROR] Failed to install dependencies.
            echo Please ensure you have internet access and run:
            echo   pip install -r requirements.txt
            echo.
            pause
            exit /b 1
        )
    )
    echo.
    echo [OK] All dependencies successfully installed!
    echo.
) else (
    echo [OK] All dependencies already satisfied.
    echo.
)

REM 5. Optional Node.js notice for satellite RailKit bridge
node --version >nul 2>&1
if errorlevel 1 (
    echo [NOTICE] Node.js not detected. Offline timetable and route graph work 100%%.
    echo          Node.js 18+ is optional for live satellite RailKit bridge.
    echo.
)

REM 6. Launch Server and Open Browser
echo [2/2] Server starting...
echo.
echo   * Landing portal : http://localhost:5000/journey
echo   * Route planner  : http://localhost:5000
echo   * Train-Dhundho  : http://localhost:5000/live
echo.
echo Opening your browser in 2 seconds. KEEP THIS WINDOW OPEN.
echo Press Ctrl+C here - or close this window - to stop the server.
echo.

start "" /b cmd /c "timeout /t 2 >nul & start http://localhost:5000/journey"

%PY_CMD% "%~dp0app.py"

if errorlevel 1 (
    echo.
    echo [ERROR] Server encountered an error and stopped.
    pause
    exit /b 1
)

echo.
echo Server stopped.
pause

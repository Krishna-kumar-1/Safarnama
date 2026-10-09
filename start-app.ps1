# Safarnama - Windows PowerShell Launcher
# Runs Safarnama with automatic dependency check and unblocking
$ErrorActionPreference = "SilentlyContinue"
Set-Location -Path $PSScriptRoot

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  🚆 Safarnama - Starting Local Server" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Unblock files in this folder if flagged by Windows Smart App Control
Get-ChildItem -Path $PSScriptRoot -Recurse | Unblock-File -ErrorAction SilentlyContinue

# Check Python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "❌ ERROR: Python was not found on your system." -ForegroundColor Red
    Write-Host "Please install Python from https://python.org and tick 'Add Python to PATH'." -ForegroundColor Yellow
    Pause
    exit 1
}

# Create .env from template if missing
if (-not (Test-Path ".env") -and (Test-Path ".env.example")) {
    Copy-Item ".env.example" ".env"
    Write-Host "ℹ️  Created .env file from .env.example" -ForegroundColor Green
}

# Verify dependencies
$check = python -c "import flask, networkx, flask_cors, cryptography" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "📦 Installing required dependencies from requirements.txt..." -ForegroundColor Yellow
    python -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install dependencies." -ForegroundColor Red
        Pause
        exit 1
    }
}

Write-Host "🚀 Server starting..." -ForegroundColor Green
Write-Host "  Landing page : http://localhost:5000/journey"
Write-Host "  Route planner: http://localhost:5000"
Write-Host ""
Write-Host "Opening your browser. KEEP THIS WINDOW OPEN." -ForegroundColor Cyan
Write-Host "Press Ctrl+C here to stop the server."
Write-Host ""

# Open browser after short delay
Start-Job -ScriptBlock { Start-Sleep -Seconds 2; Start-Process "http://localhost:5000/journey" } | Out-Null

python app.py

Pause

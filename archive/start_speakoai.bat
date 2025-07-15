@echo off
REM SpeakoAI Full Application Startup Script
REM This script starts all services: Frontend, Backend, Database, and AI Agent

echo 🚀 Starting SpeakoAI Full Application...

REM Check if Docker is running
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Docker is not installed or not running
    echo Please install Docker Desktop and start it
    pause
    exit /b 1
)

REM Check if docker-compose.yml exists
if not exist "docker-compose.yml" (
    echo ❌ Error: docker-compose.yml not found
    echo Please run this script from the root directory
    pause
    exit /b 1
)

REM Create .env file if it doesn't exist
if not exist "SpeakoAI\.env" (
    echo 📝 Creating .env file from template...
    copy "SpeakoAI\env.example" "SpeakoAI\.env"
    echo ⚠️  Please edit SpeakoAI\.env with your actual configuration
)

REM Build and start all services
echo 🏗️  Building and starting all services...
docker-compose up --build -d

if %errorlevel% equ 0 (
    echo.
    echo ✅ SpeakoAI application started successfully!
    echo.
    echo 📊 Services Status:
    echo - Frontend: http://localhost:3000
    echo - Backend API: http://localhost:8000
    echo - Database: localhost:5432
    echo - AI Agent: http://localhost:8080
    echo.
    echo 🎯 You can now access the application at: http://localhost:3000
    echo.
    echo 📋 To view logs: docker-compose logs -f
    echo 📋 To stop: docker-compose down
) else (
    echo ❌ Error: Failed to start services
    echo Check the logs with: docker-compose logs
)

pause 
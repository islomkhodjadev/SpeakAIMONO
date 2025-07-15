@echo off
REM SpeakoAI Mock Data Population Script for Windows
REM This script populates the backend database with mock data using Docker

echo 🚀 Starting SpeakoAI Mock Data Population...

REM Check if docker-compose.yml exists
if not exist "docker-compose.yml" (
    echo ❌ Error: docker-compose.yml not found in current directory
    echo Please run this script from the SpeakoAI directory
    pause
    exit /b 1
)

REM Check if the backend container is running
echo 📋 Checking if backend container is running...
docker-compose ps | findstr "backend" >nul
if errorlevel 1 (
    echo ⚠️  Backend container is not running. Starting it first...
    docker-compose up -d backend
    echo ⏳ Waiting for backend to be ready...
    timeout /t 10 /nobreak >nul
)

REM Run the population script
echo 📊 Populating database with mock data...
docker-compose exec backend python populate_mock_data.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ Mock data population completed successfully!
    echo.
    echo 📈 Summary of created data:
    echo - 5 mock users (Alice, Bob, Carol, David, Emma)
    echo - 15 IELTS speaking questions (5 for each part)
    echo - Multiple user responses with realistic scores
    echo - Feedback entries for each user
    echo.
    echo 🎯 You can now test the frontend with this mock data!
) else (
    echo ❌ Error: Failed to populate mock data
    pause
    exit /b 1
)

pause 
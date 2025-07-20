#!/bin/bash

# SpeakoAI Full Application Startup Script
# This script starts all services: Frontend, Backend, Database, and AI Agent

echo "🚀 Starting SpeakoAI Full Application..."

# Check if Docker is running
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed"
    echo "Please install Docker and start it"
    exit 1
fi

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Error: docker-compose.yml not found"
    echo "Please run this script from the root directory"
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f "SpeakoAI/.env" ]; then
    echo "📝 Creating .env file from template..."
    cp "SpeakoAI/env.example" "SpeakoAI/.env"
    echo "⚠️  Please edit SpeakoAI/.env with your actual configuration"
fi

# Build and start all services
echo "🏗️  Building and starting all services..."
docker-compose up --build -d

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SpeakoAI application started successfully!"
    echo ""
    echo "📊 Services Status:"
    echo "- Frontend: http://localhost:3000"
    echo "- Backend API: http://localhost:8000"
    echo "- Database: localhost:5432"
    echo "- AI Agent: http://localhost:8080"
    echo ""
    echo "🎯 You can now access the application at: http://localhost:3000"
    echo ""
    echo "📋 To view logs: docker-compose logs -f"
    echo "📋 To stop: docker-compose down"
else
    echo "❌ Error: Failed to start services"
    echo "Check the logs with: docker-compose logs"
    exit 1
fi 
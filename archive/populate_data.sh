#!/bin/bash

# SpeakoAI Mock Data Population Script
# This script populates the backend database with mock data using Docker

echo "🚀 Starting SpeakoAI Mock Data Population..."

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Error: docker-compose.yml not found in current directory"
    echo "Please run this script from the SpeakoAI directory"
    exit 1
fi

# Check if the backend container is running
echo "📋 Checking if backend container is running..."
if ! docker-compose ps | grep -q "backend"; then
    echo "⚠️  Backend container is not running. Starting it first..."
    docker-compose up -d backend
    echo "⏳ Waiting for backend to be ready..."
    sleep 10
fi

# Run the population script
echo "📊 Populating database with mock data..."
docker-compose exec backend python populate_mock_data.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Mock data population completed successfully!"
    echo ""
    echo "📈 Summary of created data:"
    echo "- 5 mock users (Alice, Bob, Carol, David, Emma)"
    echo "- 15 IELTS speaking questions (5 for each part)"
    echo "- Multiple user responses with realistic scores"
    echo "- Feedback entries for each user"
    echo ""
    echo "🎯 You can now test the frontend with this mock data!"
else
    echo "❌ Error: Failed to populate mock data"
    exit 1
fi 
#!/bin/bash

# Production deployment script for SpeakoAI

set -e

echo "🚀 Starting production deployment..."

# Check if required files exist
if [ ! -f ".env.prod" ]; then
    echo "❌ .env.prod file not found!"
    echo "Please create .env.prod with production environment variables"
    exit 1
fi

if [ ! -f "docker-compose.prod.yml" ]; then
    echo "❌ docker-compose.prod.yml not found!"
    exit 1
fi

# Pull latest changes
echo "📥 Pulling latest changes..."
git pull origin main

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker-compose -f docker-compose.prod.yml down

# Remove old images (optional - comment out if you want to keep them)
echo "🧹 Cleaning up old images..."
docker system prune -f

# Build and start containers
echo "🔨 Building and starting containers..."
docker-compose -f docker-compose.prod.yml up -d --build

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 30

# Check if services are running
echo "🔍 Checking service health..."
docker-compose -f docker-compose.prod.yml ps

# Test API endpoint
echo "🧪 Testing API endpoint..."
if curl -f http://localhost/api/health > /dev/null 2>&1; then
    echo "✅ API is responding!"
else
    echo "❌ API is not responding!"
    echo "Check logs with: docker-compose -f docker-compose.prod.yml logs"
fi

# Show running containers
echo "📊 Running containers:"
docker-compose -f docker-compose.prod.yml ps

echo "🎉 Deployment complete!"
echo ""
echo "🔗 Your app should be available at:"
echo "   Frontend: https://your-domain.com"
echo "   API: https://your-domain.com/api"
echo ""
echo "📝 Useful commands:"
echo "   View logs: docker-compose -f docker-compose.prod.yml logs -f"
echo "   Stop services: docker-compose -f docker-compose.prod.yml down"
echo "   Restart: docker-compose -f docker-compose.prod.yml restart"
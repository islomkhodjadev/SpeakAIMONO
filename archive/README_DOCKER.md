## For powershell, to get data for db container
```bash
Get-Content ./archive/populate_mock_data_fixed.sql | docker exec -i speakoai-db psql -U postgres -d miniapp
```


## Everything below is absolute bullshit



# SpeakoAI Docker Setup

This document explains how to run the complete SpeakoAI application using Docker, including the frontend, backend, database, and Go AI agent.

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Frontend   │    │   Backend   │    │   Database  │    │  AI Agent   │
│  (React)    │◄──►│  (FastAPI)  │◄──►│ (PostgreSQL)│    │   (Go)      │
│  Port 3000  │    │  Port 8000  │    │  Port 5432  │    │  Port 8080  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## 🚀 Quick Start

### Windows Users
```bash
# Run the startup script
start_speakoai.bat
```

### Linux/Mac Users
```bash
# Make script executable
chmod +x start_speakoai.sh

# Run the startup script
./start_speakoai.sh
```

### Manual Start
```bash
# Build and start all services
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## 📁 Project Structure

```
full app/
├── docker-compose.yml          # Global Docker Compose
├── start_speakoai.bat         # Windows startup script
├── start_speakoai.sh          # Linux/Mac startup script
├── SpeakoAI/
│   ├── backend/               # FastAPI backend
│   ├── ai-agent/              # Go AI agent (needs to be created)
│   ├── .env                   # Environment variables
│   ├── env.example            # Environment template
│   └── Dockerfile             # Backend Dockerfile
└── SpeakoAIfront/
    └── speakoai/
        ├── src/               # React frontend
        └── Dockerfile         # Frontend Dockerfile
```

## 🔧 Services

### 1. Frontend (React + Vite)
- **Port**: 3000
- **URL**: http://localhost:3000
- **Technology**: React, Vite, TailwindCSS
- **Container**: speakoai-frontend

### 2. Backend (FastAPI)
- **Port**: 8000
- **URL**: http://localhost:8000
- **Technology**: Python, FastAPI, SQLAlchemy
- **Container**: speakoai-backend

### 3. Database (PostgreSQL)
- **Port**: 5432
- **Database**: miniapp
- **Username**: postgres
- **Password**: admin1234
- **Container**: speakoai-db

### 4. AI Agent (Go)
- **Port**: 8080
- **URL**: http://localhost:8080
- **Technology**: Go
- **Container**: speakoai-ai-agent

### 5. Telegram Bot (Optional)
- **Technology**: Python
- **Container**: speakoai-telegram-bot

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `SpeakoAI/` directory:

```bash
# Database Configuration
DATABASE_URL=postgresql+asyncpg://postgres:admin1234@db:5432/miniapp

# AI Agent Configuration
AI_AGENT_URL=http://ai-agent:8080

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Frontend Configuration
FRONTEND_URL=http://localhost:3000

# Environment
ENVIRONMENT=production
DEBUG=false
```

## 🐳 Docker Commands

### Start Services
```bash
# Start all services
docker-compose up -d

# Start with logs
docker-compose up

# Rebuild and start
docker-compose up --build -d
```

### Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### View Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
docker-compose logs ai-agent

# Follow logs in real-time
docker-compose logs -f
```

### Access Services
```bash
# Access backend container
docker-compose exec backend bash

# Access database
docker-compose exec db psql -U postgres -d miniapp

# Access frontend container
docker-compose exec frontend sh
```

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Check what's using the port
   netstat -ano | findstr :3000
   # Kill the process or change ports in docker-compose.yml
   ```

2. **Database connection issues**
   ```bash
   # Check if database is running
   docker-compose ps
   # Restart database
   docker-compose restart db
   ```

3. **Frontend not loading**
   ```bash
   # Check frontend logs
   docker-compose logs frontend
   # Rebuild frontend
   docker-compose build frontend
   ```

4. **AI Agent not responding**
   ```bash
   # Check AI agent logs
   docker-compose logs ai-agent
   # Test AI agent directly
   curl http://localhost:8080/health
   ```

### Reset Everything
```bash
# Stop and remove everything
docker-compose down -v --remove-orphans

# Remove all images
docker system prune -a

# Start fresh
docker-compose up --build -d
```

## 📊 Monitoring

### Check Service Status
```bash
# View running containers
docker-compose ps

# View resource usage
docker stats
```

### Database Operations
```bash
# Run SQL script
docker-compose exec db psql -U postgres -d miniapp -f /docker-entrypoint-initdb.d/init.sql

# Backup database
docker-compose exec db pg_dump -U postgres miniapp > backup.sql

# Restore database
docker-compose exec -T db psql -U postgres -d miniapp < backup.sql
```

## 🔄 Development Workflow

### Making Changes

1. **Frontend Changes**
   ```bash
   # The frontend volume is mounted, changes are reflected immediately
   # Rebuild if needed
   docker-compose build frontend
   ```

2. **Backend Changes**
   ```bash
   # Backend code is mounted, restart the service
   docker-compose restart backend
   ```

3. **AI Agent Changes**
   ```bash
   # Rebuild AI agent
   docker-compose build ai-agent
   docker-compose up -d ai-agent
   ```

### Adding New Services

1. Add service to `docker-compose.yml`
2. Create Dockerfile for the service
3. Update environment variables if needed
4. Rebuild and start: `docker-compose up --build -d`

## 🎯 Next Steps

1. **Set up the Go AI Agent**: Create the Go application in `SpeakoAI/ai-agent/`
2. **Configure Environment**: Edit `SpeakoAI/.env` with your actual values
3. **Test the Application**: Access http://localhost:3000
4. **Monitor Logs**: Use `docker-compose logs -f` to monitor all services

## 📞 Support

If you encounter issues:
1. Check the logs: `docker-compose logs`
2. Verify all services are running: `docker-compose ps`
3. Check the troubleshooting section above
4. Ensure Docker Desktop is running and has enough resources 
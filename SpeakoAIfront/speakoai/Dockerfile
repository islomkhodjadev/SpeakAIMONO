# Frontend Dockerfile for SpeakoAI
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install all dependencies (including dev dependencies for build)
RUN npm ci

# Copy source code
COPY . .
RUN npm install react-markdown
RUN npm install -D @tailwindcss/typography

# Build the app
RUN npm run build

# Install serve globally
RUN npm install -g serve

# Expose port
EXPOSE 3000

# Start the app with serve
CMD ["serve", "-s", "dist", "-l", "3000"] 
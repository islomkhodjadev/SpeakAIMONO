# Go AI Agent Dockerfile for SpeakoAI
FROM golang:1.23-alpine AS builder

# Set working directory
WORKDIR /app
RUN go mod init main
# Copy go mod files
COPY go.mod go.sum ./

# Initialize module and download dependencies
RUN go mod download
RUN go mod tidy

# Copy source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o ai_agent .

# Final stage
FROM alpine:latest

# Install ca-certificates for HTTPS requests
RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Copy the binary from builder stage
COPY --from=builder /app/ai_agent .

# Expose port
EXPOSE 8080

# Run the binary
CMD ["./ai_agent"] 
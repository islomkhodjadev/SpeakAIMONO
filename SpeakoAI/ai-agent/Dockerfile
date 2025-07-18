# Start from the official Golang image for building
FROM golang:1.23 as builder

WORKDIR /app

# Copy go mod and sum files
COPY go.mod go.sum ./
RUN go mod download
# Copy the rest of the source code
COPY . .

# Build the Go app (output to /app/build/app)
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/build/app ./cmd/main.go

# Use a minimal base image for running
FROM alpine:latest
WORKDIR /root/

# Copy the built binary from the builder
COPY --from=builder /app/build/app .
COPY --from=builder /app/docs ./docs

# Expose the port your app runs on
EXPOSE 8085

# Command to run the executable
CMD ["./app"] 
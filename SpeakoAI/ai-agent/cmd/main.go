// @title           AI Agent API
// @version         1.0
// @description     API for managing AI scoring sessions and answers using chi and net/http.
// @host            localhost:8080
// @BasePath        /
package main

import (
	"aiagent/internal/handlers"
	"aiagent/internal/router"
	"context"
	"log"
	"net/http"
	"os"

	_ "aiagent/docs"

	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
)

type Config struct {
	Addr string
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Println("No .env file found, assuming production environment")
	}
	githubToken := os.Getenv("AI_API")

	app := &Config{Addr: ":8085"}

	redis_client := redis.NewClient(
		&redis.Options{
			Addr:     "redis:6379",
			Password: "",
			DB:       0,
			Protocol: 2,
		},
	)
	pong, err := redis_client.Ping(context.Background()).Result()
	if err != nil {
		log.Fatalf("Could not connect to Redis: %v", err)
	}
	log.Printf("Redis connected successfully: %s", pong)
	log.Println("redis connected at port :6379")

	handlerConfig := handlers.HandlerConfig{
		RedisClient: redis_client,
		GithubToken: githubToken,
	}

	router := router.CreateRouterWithHandlers(&handlerConfig)

	log.Printf("Server starting on %s\n", app.Addr)

	server := &http.Server{
		Addr:    app.Addr,
		Handler: router,
	}
	err = server.ListenAndServe()
	if err != nil {
		log.Fatal("Server failed:", err)
	}
}

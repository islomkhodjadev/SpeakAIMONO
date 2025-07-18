package handlers

import "github.com/redis/go-redis/v9"

type HandlerConfig struct {
	RedisClient *redis.Client
	GithubToken string
}

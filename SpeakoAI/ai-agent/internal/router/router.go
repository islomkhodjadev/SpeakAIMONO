package router

import (
	"aiagent/internal/handlers"
	"aiagent/internal/middlewares"

	"github.com/go-chi/chi/v5"
	httpSwagger "github.com/swaggo/http-swagger"
)

func CreateRouterWithHandlers(handlerConfig *handlers.HandlerConfig) *chi.Mux {
	r := chi.NewRouter()
	r.Use(middlewares.LoggingMiddleware)
	r.Post("v1/score", handlerConfig.Score)
	r.Post("v1/start-session", handlerConfig.StartSession)
	r.Post("v1/add-answer", handlerConfig.PostAnswer)
	// Swagger UI route
	r.Get("/swagger/*", httpSwagger.WrapHandler)

	return r
}

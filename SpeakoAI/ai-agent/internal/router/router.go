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
	r.Post("/score", handlerConfig.Score)
	r.Post("/start-session", handlerConfig.StartSession)
	r.Post("/add-answer", handlerConfig.PostAnswer)
	// Swagger UI route
	r.Get("/swagger/*", httpSwagger.WrapHandler)

	return r
}

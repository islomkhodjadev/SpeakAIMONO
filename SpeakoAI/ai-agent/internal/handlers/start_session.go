package handlers

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
)

type StartSessionRequest struct {
	UserID string `json:"user_id" example:"123"`
}

type StartSessionResponse struct {
	Error   string `json:"error" example:"false"`
	Success string `json:"success" example:"true"`
}

// StartSession godoc
// @Summary      Start a new user session
// @Description  Initializes a new session for the user in Redis
// @Tags         session
// @Accept       json
// @Produce      json
// @Param        request  body  StartSessionRequest  true  "User ID payload"
// @Success      202  {object}  StartSessionResponse  "Session started"
// @Failure      400  {string}  string  "Missing or invalid user_id"
// @Router       /start-session [post]
func (config *HandlerConfig) StartSession(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	var data map[string]interface{}
	json.NewDecoder(r.Body).Decode(&data)

	user_id, ok := data["user_id"].(string)
	if !ok {
		log.Println("user_id is not string")
		http.Error(w, "Missing or invalid user_id", http.StatusBadRequest)

		return
	}
	ctx := context.Background()

	err := config.RedisClient.Set(ctx, user_id, "", 0).Err()
	if err != nil {
		log.Println(err)
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	w.Write([]byte(`{"error": "false", "success": "true"}`))
}

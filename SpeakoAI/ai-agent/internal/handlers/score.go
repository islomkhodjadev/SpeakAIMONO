package handlers

import (
	"aiagent/internal/gpt"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
)

// ScoreRequest defines the expected input for the /score endpoint
type ScoreRequest struct {
	UserID string `json:"user_id" example:"123"`
}

// ScoreResponse defines the expected response from the /score endpoint
type ScoreResponse struct {
	Answer string `json:"answer" example:"You performed well!"`
}

// Score godoc
// @Summary      Get AI score for a user session
// @Description  Returns an AI-generated score for the user's session data
// @Tags         score
// @Accept       json
// @Produce      json
// @Param        request body ScoreRequest true "User ID"
// @Success      200 {object} ScoreResponse
// @Failure      400 {string} string "not found id"
// @Failure      500 {string} string "Failed to marshal response"
// @Router       /score [post]
func (config *HandlerConfig) Score(w http.ResponseWriter, r *http.Request) {

	ctx := context.Background()
	var data map[string]interface{}

	json.NewDecoder(r.Body).Decode(&data)

	user_id, ok := data["user_id"].(string)

	if !ok {
		http.Error(w, "not found id", http.StatusBadRequest)
		return
	}

	val, err := config.RedisClient.Get(ctx, user_id).Result()

	if err != nil {
		http.Error(w, "not found id", http.StatusBadRequest)
		return
	}
	config.RedisClient.Del(ctx, user_id)

	fmt.Println(val)

	result := gpt.GetAIResponse(val, config.GithubToken)
	w.Header().Set("Content-Type", "application/json")
	jsonResponse := map[string]string{
		"answer": result,
	}

	responseBytes, err := json.Marshal(jsonResponse)
	if err != nil {
		http.Error(w, "Failed to marshal response", http.StatusInternalServerError)
		return
	}

	w.Write(responseBytes)
}

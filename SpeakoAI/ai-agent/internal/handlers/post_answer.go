package handlers

import (
	"aiagent/internal/models"
	"context"
	"encoding/json"
	"net/http"
	"strconv"
)

// PostAnswer godoc
// @Summary      Add an answer to the user session
// @Description  Adds an answer to the user's session data in Redis
// @Tags         answer
// @Accept       json
// @Produce      json
// @Param        answer  body  models.AnswerRequest  true  "Answer payload"
// @Success      200  {object}  models.UserData
// @Failure      400  {string}  string  "Invalid Json or Error getting user session"
// @Failure      500  {string}  string  "Error marshalling or saving updated user data"
// @Router       /add-answer [post]
func (config *HandlerConfig) PostAnswer(w http.ResponseWriter, r *http.Request) {
	var answer models.AnswerRequest
	err := json.NewDecoder(r.Body).Decode(&answer)

	if err != nil {
		http.Error(w, "Invalid Json"+err.Error(), http.StatusBadRequest)
		return
	}

	ctx := context.Background()

	var user_data models.UserData

	user_id := strconv.Itoa(answer.UserID)
	val, err := config.RedisClient.Get(ctx, user_id).Result()

	if err != nil {
		http.Error(w, "Error getting user session", http.StatusBadRequest)
		return
	}

	json.Unmarshal([]byte(val), &user_data)
	user_data.AddAnswer(&answer)
	updated_json, err := json.Marshal(user_data)
	if err != nil {
		http.Error(w, "Error marshalling updated user data: "+err.Error(), http.StatusInternalServerError)
		return
	}
	err = config.RedisClient.Set(ctx, user_id, updated_json, 0).Err()

	if err != nil {
		http.Error(w, "Error saving updated user session: "+err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(updated_json))

}

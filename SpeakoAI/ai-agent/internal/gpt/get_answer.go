package gpt

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

func GetAIResponse(user_content, githubToken string) string {
	url := "https://models.github.ai/inference/chat/completions"

	// Define the request body structure
	payload := map[string]interface{}{
		"messages": []map[string]string{
			{
				"role": "system",
				"content": `
								First of all write full answer within 200 words thats it.
								Evaluate the speaking performance of the candidate based on the IELTS Speaking Band Descriptors criteria provided. 
								The candidate’s speaking responses are given in JSON format structured by parts and questions. 
								Parse and analyze each response precisely and concisely without extraneous commentary.
								For each part (Part 1, Part 2, Part 3), provide strictly the following:

								1. **Fluency and Coherence Score (1-9)**: Brief justification using specific examples.
								2. **Lexical Resource Score (1-9)**: Brief justification using specific examples.
								3. **Grammatical Range and Accuracy Score (1-9)**: Brief justification using specific examples.
								4. **Pronunciation Score (1-9)**: Brief justification using specific examples.

								Calculate and state clearly an average band score for each part.

								Finally, present an overall band score calculated as 
								the average of the band scores for all three parts, 
								summarizing succinctly the candidate's main strengths and key areas for improvement. 
								`,
			},
			{
				"role":    "user",
				"content": user_content,
			},
		},
		"model":       "openai/gpt-4o-mini",
		"temperature": 0.3,
		"max_tokens":  500,
		"top_p":       0.8,
	}

	jsonData, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		panic(err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+githubToken)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Read and print response
	bodyBytes, _ := io.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(bodyBytes, &result)

	// Log the raw response (useful for debugging)
	fmt.Println("Raw response:", string(bodyBytes))

	choices, ok := result["choices"].([]interface{})
	if !ok || len(choices) == 0 {
		log.Println("API Error or Unexpected Response Format:", string(bodyBytes))
		return "Error: invalid response from scoring engine"
	}

	message, ok := choices[0].(map[string]interface{})["message"].(map[string]interface{})
	if !ok {
		log.Println("Error reading message field:", string(bodyBytes))
		return "Error: invalid message format"
	}

	content, ok := message["content"].(string)
	if !ok {
		log.Println("Content missing in message:", string(bodyBytes))
		return "Error: content missing"
	}

	return content

}

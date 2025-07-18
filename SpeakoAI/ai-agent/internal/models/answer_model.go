package models

type UserData struct {
	// UserID int    `json:"user_id"`
	Part []Part `json:"part"`
}

func (u *UserData) AddAnswer(answer *AnswerRequest) {
	newAnswer := Answer{
		Answer:   answer.Answer,
		Question: answer.Question,
	}
	for i := range u.Part {
		if u.Part[i].Number == answer.Part {
			u.Part[i].Answer = append(u.Part[i].Answer, newAnswer)
			return
		}
	}

	newPart := Part{
		Number: answer.Part,
		Answer: []Answer{newAnswer},
	}
	u.Part = append(u.Part, newPart)

}

type Part struct {
	Number int      `json:"number"`
	Answer []Answer `json:"answer"`
}

type Answer struct {
	Question string `json:"question"`
	Answer   string `json:"answer"`
}

type AnswerRequest struct {
	UserID   int    `json:"user_id"`
	Part     int    `json:"part"`
	Question string `json:"question"`
	Answer   string `json:"answer"`
}

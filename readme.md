
# 🧠 SpeakAI Mini App — Dev Setup

## ⚙️ Project Setup Guidelines

> **Heads Up:**
> `.env` file **must be placed in the project root directory** — no exceptions.



### 🧪 Load questions from JSON into DB

Inside the **backend container**, execute: - > this fulls your db with questions and categories

```bash
cd /app
PYTHONPATH=. python SpeakoAI/backend/scripts/json2db.py
```
```bash
cd /app
PYTHONPATH=. python SpeakoAI/backend/scripts/json2db_cat.py

```

To be able to create categories and questions through swagger:

```bash
SELECT setval('categories_id_seq', (SELECT MAX(id) FROM categories));
SELECT setval('questions_id_seq', (SELECT MAX(id) FROM questions));
```
---




## 🌐 Local Project URLs

| Service        | URL                                                                                  |
| -------------- | ------------------------------------------------------------------------------------ |
| 🖥️ Frontend   | [http://localhost:3000/](http://localhost:3000/)                                     |
| 🤖 AI Agent    | [http://localhost:8085/swagger/index.html](http://localhost:8085/swagger/index.html) |
| 🧩 Backend API | [http://localhost:8000/docs](http://localhost:8000/docs)                             |

---

## ✨ Code Quality with `ruff`

### Lint & Auto-fix

```bash
ruff check . --fix
```

### Format Code (like `black`)

```bash
ruff format .
```

---

Let me know if you want badges, license, docker instructions, or contributor section added. This is lean, but sharp.

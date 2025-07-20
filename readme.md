
# 🧠 SpeakAI Mini App — Dev Setup

## 🛠️ Project Guidelines

1. `.env` file **must be placed in the root directory only**.
2. To populate the PostgreSQL database from PowerShell, run:

   ```bash
   Get-Content ./archive/populate_mock_data_fixed.sql | docker exec -i speakoai-db psql -U postgres -d miniapp
   ```
3. ⚠️ **Avoid adding unnecessary files** outside the frontend directory. Keep the repo clean and organized.



## 🌐 Project URLs (Local)

* **Frontend:** [http://localhost:3000/](http://localhost:3000/)
* **AI Agent (Whisper + GPT):** [http://localhost:8085/swagger/index.html](http://localhost:8085/swagger/index.html)
* **Backend API (FastAPI):** [http://localhost:8000/docs](http://localhost:8000/docs)

---





## 🚀 ruff usage

Check and fix all files:

```bash
ruff check . --fix
```

Or format code (like `black`):

```bash
ruff format .
```

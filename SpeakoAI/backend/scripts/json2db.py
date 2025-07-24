# scripts/json2db.py

import asyncio
import json
import os
import sys

# Adds /app/SpeakoAI/backend to sys.path no matter where script is run from
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(project_root)
from SpeakoAI.backend.models.tables.question import (
    Question,  # make sure this is right path
)
from SpeakoAI.backend.models.tables.question import (
    Question,  # make sure this is right path
)
from SpeakoAI.backend.services.conn import connection


@connection
async def insert_questions(session):
    # 🚧 Step 1: Load JSON file
    import os

    json_path = os.path.join(os.path.dirname(__file__), "questions", "question.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 🚧 Step 2: Insert each question
    for item in data:
        item["extra_text"] = item.get("extra_text") or None
        q = Question(**item)
        session.add(q)

    # 🚧 Step 3: Commit changes
    await session.commit()
    print("✅ All questions committed to DB!")

# 🚧 Step 4: Run it
if __name__ == "__main__":
    asyncio.run(insert_questions())

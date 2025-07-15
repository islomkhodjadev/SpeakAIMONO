import httpx
from fastapi import APIRouter, Form

from backend.core.config import settings
from backend.models.schemas.schemas import ScoreRequests, ScoreResponse
from backend.services.audio.voice_transcription import download_voice, voice2text

router = APIRouter(prefix="/api/ai", tags=["AI Agent"])


@router.post("/score-voice", response_model=ScoreResponse)
async def get_score_voice(req: ScoreRequests):
    file_id: str = Form(...)
    user_id: str = Form(...)
    try:
        async with httpx.AsyncClient() as client:
            from aiogram import Bot
            bot = Bot(token=settings.BOT_TOKEN)
            save_path = f"voices/{user_id}.ogg"
            await download_voice(bot, file_id, save_path)

            transcript = await voice2text((save_path))

            payload = {"question": transcript}
            async with httpx.AsyncClient() as client:
                resp = await client.post("http://host.docker.internal:8080/score", json=payload)
                resp.raise_for_status()
                score = resp.json().get("score")

            return {
                "text": transcript,
                "score": score,
            }



    except httpx.HTTPError as e:
        return {"score": f"Something wrong with ai: {str(e)}"}
    except Exception as e:
        print(f"General error: {str(e)}")
        return {"score": f"Something wrong with ai: {str(e)}"}

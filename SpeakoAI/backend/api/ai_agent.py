from fastapi import APIRouter
from pydantic import BaseModel
import httpx
from backend.models.schemas.schemas import ScoreRequests, ScoreResponse

router = APIRouter(prefix="/api/ai", tags=["AI Agent"])


@router.post("/score", response_model=ScoreResponse)
async def get_score(req: ScoreRequests):
    try:
        async with httpx.AsyncClient() as client:
            # Use Docker service name for internal communication
            response = await client.post("http://ai-agent:8085/score", json=req.dict())

            response.raise_for_status()

            raw = response.json()
            score = raw.get("score", "Something went wrong. No score returned.")
            print(f"Score : {score}")
            return {"score": score}

    except httpx.HTTPError as e:
        return {"score": f"Something wrong with ai: {str(e)}"}
    except Exception as e:
        print(f"General error: {str(e)}")
        return {"score": f"Something wrong with ai: {str(e)}"}

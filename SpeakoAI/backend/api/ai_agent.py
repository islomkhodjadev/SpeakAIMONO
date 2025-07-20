import logging
from typing import Optional

import httpx
from backend.models.schemas.schemas import ScoreScheme, StartScheme, UserResponseCreateSchema
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse
from backend.services.requests.user_response import create_user_response

router = APIRouter(prefix="/api/ai", tags=["AI Agent"])

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Configuration
AI_SERVICE_TIMEOUT = {
    "start_session": 30.0,
    "add_answer": 60.0,
    "score": 120.0
}


@router.post("/start-session")
async def start_session(req: StartScheme):
    url = "http://ai-agent:8085/v1/start-session"
    payload = req.dict()

    logger.info(f"📤 Sending POST request to AI Agent: {url}")
    logger.info(f"📦 Payload: {payload}")

    try:
        timeout = httpx.Timeout(AI_SERVICE_TIMEOUT["start_session"])
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()

            logger.info(f"✅ Response Status Code: {response.status_code}")
            logger.info(f"📥 Response Body: {response.text}")

            data = response.json()
            return {"res": data}

    except httpx.TimeoutException as e:
        logger.error(f"⏰ Timeout error: {str(e)}")
        return JSONResponse(status_code=504, content={
            "error": "AI service timeout during session start"
        })

    except httpx.RequestError as e:
        logger.error(f"❌ Connection error: {e}")
        return JSONResponse(status_code=502, content={
            "error": f"Connection error: {e}"
        })

    except httpx.HTTPStatusError as e:
        logger.error(f"🚨 Bad response: {e.response.status_code} - {e.response.text}")
        return JSONResponse(status_code=e.response.status_code, content={
            "error": f"Bad response from AI agent: {e.response.status_code} - {e.response.text}"
        })

    except Exception as e:
        logger.exception(f"🔥 Unhandled error: {str(e)}")
        return JSONResponse(status_code=500, content={
            "error": f"Unhandled error: {str(e)}"
        })


@router.post("/add-answer")
async def add_answer(
        file: UploadFile = File(...),
        user_id: str = Form(...),
        part: int = Form(...),
        question: Optional[str] = Form(None),
):
    try:
        transcribe_timeout = httpx.Timeout(120.0)
        async with httpx.AsyncClient(timeout=transcribe_timeout) as client:
            transcribe_resp = await client.post(
                "http://127.0.0.1:8000/transcribe",
                files={"file": (file.filename, await file.read(), file.content_type)}
            )

        transcribe_resp.raise_for_status()
        text = transcribe_resp.json().get("text")
        logger.info(f"Transcribed text: {text}")

        if not text:
            return JSONResponse(status_code=400, content={"error": "Transcription failed"})

        # 2. Send transcribed answer to AI agent
        payload = {
            "answer": text,
            "user_id": str(user_id),
            "part": part,
            "question": question
        }

        response_data = UserResponseCreateSchema(
            user_id=str(user_id),
            part=part,
            question=question,
            answer=text,
        )
        await create_user_response(response_data=response_data)
        ai_timeout = httpx.Timeout(AI_SERVICE_TIMEOUT["add_answer"])
        async with httpx.AsyncClient(timeout=ai_timeout) as client:
            collect_resp = await client.post("http://ai-agent:8085/v1/add-answer", json=payload)
            collect_resp.raise_for_status()

        return {"status": "success", "message": "Answer collected"}

    except httpx.TimeoutException as e:
        logger.error(f"⏰ Timeout error: {str(e)}")
        return JSONResponse(status_code=504, content={"error": "Service timeout - please try again"})

    except httpx.HTTPError as e:
        logger.error(f"HTTP error: {str(e)}")
        return JSONResponse(status_code=500, content={"error": f"HTTP error: {str(e)}"})

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.post("/score")
async def get_score(score: ScoreScheme):
    url = "http://ai-agent:8085/v1/score"
    payload = score.dict()

    logger.info(f"📤 Sending POST request to AI Agent: {url}")
    logger.info(f"📦 Payload: {payload}")

    try:
        # Set a longer timeout for AI scoring (2 minutes)
        timeout = httpx.Timeout(AI_SERVICE_TIMEOUT["score"])

        async with httpx.AsyncClient(timeout=timeout) as client:
            logger.info("🚀 Making request with extended timeout (120s)...")
            response = await client.post(url, json=payload)
            response.raise_for_status()

            logger.info(f"✅ Response Status Code: {response.status_code}")
            logger.info(f"📥 Response Body: {response.text}")

            data = response.json()
            return data

    except httpx.TimeoutException as e:
        logger.error(f"⏰ Timeout error after {AI_SERVICE_TIMEOUT['score']} seconds: {str(e)}")
        return JSONResponse(status_code=504, content={
            "error": "AI scoring is taking longer than expected. Please try again.",
            "details": f"The AI evaluation process timed out after {AI_SERVICE_TIMEOUT['score']} seconds."
        })

    except httpx.ConnectError as e:
        logger.error(f"❌ Connection error (ConnectError): {str(e)}")
        return JSONResponse(status_code=502, content={
            "error": f"Cannot connect to AI service at {url}. Is the service running?",
            "details": str(e)
        })

    except httpx.RequestError as e:
        logger.error(f"❌ Request error: {str(e)}")
        return JSONResponse(status_code=502, content={
            "error": f"Request error: {str(e)}",
            "error_type": type(e).__name__
        })

    except httpx.HTTPStatusError as e:
        logger.error(f"🚨 HTTP Status error: {e.response.status_code}")
        logger.error(f"📄 Response text: {e.response.text}")
        return JSONResponse(status_code=e.response.status_code, content={
            "error": f"AI service returned error: {e.response.status_code}",
            "details": e.response.text
        })

    except Exception as e:
        logger.exception(f"🔥 Unhandled error: {str(e)}")
        return JSONResponse(status_code=500, content={
            "error": f"Unhandled error: {str(e)}",
            "error_type": type(e).__name__
        })

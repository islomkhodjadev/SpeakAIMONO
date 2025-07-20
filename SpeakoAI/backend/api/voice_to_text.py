import os
import uuid

import assemblyai as aai
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from ..core.config import settings

router = APIRouter()



aai.settings.api_key = settings.VOICE2TEXT




@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:

        file_ext = os.path.splitext(file.filename)[-1]

        temp_filename = f"temp_{uuid.uuid4().hex}{file_ext}"
        file_path = f"temp_audio/{temp_filename}"
        os.makedirs("temp_audio", exist_ok=True)

        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)


        config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)
        transcriber = aai.Transcriber(config=config)

        transcript = transcriber.transcribe(file_path)


        # Clean up
        # os.remove(file_path)

        if transcript.status == "error":
            print(f"❌ Transcription failed: {transcript.error}")
            raise RuntimeError(f"Transcription failed: {transcript.error}")

        print(f"📤 Transcription result: {transcript.text[:200]}...")  # first 200 chars
        return {"text": transcript.text}

    except Exception as e:
        print(f"[!] Transcription error: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": "Something went wrong during transcription."}
        )


import asyncio
import os

import aiofiles
import aiohttp
import assemblyai as aai

from SpeakoAI.config import settings

aai.settings.api_key = settings.VOICE2TEXT


async def voice2text(request):
    try:
        config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)
        transcript = aai.Transcriber(config=config).transcribe(request)

        if transcript.status == "error":
            raise RuntimeError(f"Transcription failed: {transcript.error}")

        return transcript.text

    except Exception as e:
        print(f"[!] voice to text Exception: {e}")
        return "Error: Something went wrong."




async def download_voice(bot, file_id: str, save_path: str) -> str:
    try:
        file = await bot.get_file(file_id)
        file_path = getattr(file, "file_path", None)

        if not file_path:
            raise Exception("file_path is None. Failed to retrieve from Telegram.")

        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as resp:
                if resp.status == 200:
                    async with aiofiles.open(save_path, mode='wb') as f:
                        await f.write(await resp.read())
                    return save_path
                else:
                    raise Exception(f"Failed to download file: Status {resp.status}")

    except Exception as e:
        print(f"[!] Error in download_voice: {e}")
        raise

if __name__ == "__main__":
    async def main():
        path = "sample.ogg"
        output = await voice2text(path)
        print("text version:", output)


    asyncio.run(main())















import asyncio
from tempfile import NamedTemporaryFile

import openai
from pydub import AudioSegment


# ---------------------
# ✅ Your original code
# ---------------------
async def download_voice(bot, file_id: str, save_path: str) -> str:
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status == 200:
                async with aiofiles.open(save_path, mode='wb') as f:
                    await f.write(await resp.read())
                return save_path
            else:
                raise Exception("Failed to download file")


# ---------------------
# 🔊 Convert to .wav
# ---------------------
def convert_to_wav(ogg_path: str) -> str:
    sound = AudioSegment.from_ogg(ogg_path)

    wav_file = NamedTemporaryFile(suffix=".wav", delete=False)
    wav_path = wav_file.name
    sound.export(wav_path, format="wav")

    return wav_path


# ---------------------
# 🤖 Transcribe using Whisper
# ---------------------
async def transcribe_voice(wav_path: str) -> str:
    try:
        with open(wav_path, "rb") as audio_file:
            transcript = await asyncio.to_thread(
                openai.Audio.transcribe,
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return transcript
    except Exception as e:
        print(f"[!] voice to text Exception: {e}")
        return "Error: Something went wrong."


# ---------------------
# 🔁 Whole process
# ---------------------
import shutil
import tempfile
import uuid

import whisper
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()
model = whisper.load_model("base")  # Or "small", "medium", "large" depending on your resources

@router.post("/voice-to-text")
async def voice_to_text(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be an audio type")

    try:
        # Save to a temporary location
        with tempfile.TemporaryDirectory() as tmp_dir:
            original_path = os.path.join(tmp_dir, f"{uuid.uuid4()}.webm")
            with open(original_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Convert to wav
            wav_path = original_path.replace(".webm", ".wav")
            sound = AudioSegment.from_file(original_path)
            sound.export(wav_path, format="wav")

            # Transcribe
            result = model.transcribe(wav_path)
            transcript = result.get("text", "").strip()

            return JSONResponse({"text": transcript})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

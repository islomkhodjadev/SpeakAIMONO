import asyncio
import os

import aiofiles
import aiohttp
import assemblyai as aai

from backend.core.config import settings

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


if __name__ == "__main__":
    async def main():
        path = "audio_2025-07-11_08-44-43.ogg"
        output = await voice2text(path)
        print("text version:", output)


    asyncio.run(main())

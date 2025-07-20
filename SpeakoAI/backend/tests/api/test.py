import asyncio

import assemblyai as aai
from config import settings

aai.settings.api_key = settings.VOICE2TEXT

async def transcribe_audio_file(file_path: str):
    try:
        config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)
        transcriber = aai.Transcriber(config=config)
        transcript =  transcriber.transcribe(file_path)

        if transcript.status == "error":
            raise RuntimeError(f"Transcription failed: {transcript.error}")

        return transcript.text

    except Exception as e:
        print(f"[!] Transcription error: {e}")
        return None
if __name__ == '__main__':
    path = 'sample.ogg'

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(transcribe_audio_file(path))
    print(result)

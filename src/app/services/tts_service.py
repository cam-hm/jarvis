import edge_tts
import tempfile
import os

class TTSService:
    def __init__(self):
        # Jarvis-like voice (British Male)
        self.voice = "en-GB-RyanNeural"

    async def generate_audio(self, text: str) -> bytes:
        communicate = edge_tts.Communicate(text, self.voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data

tts_service = TTSService()

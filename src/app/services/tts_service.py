from piper import PiperVoice
import io
import wave
import tempfile
import os

class TTSService:
    def __init__(self):
        # Path to Jarvis Piper model (high quality)
        self.model_path = "src/app/services/models/jarvis/jarvis-high.onnx"
        self.config_path = "src/app/services/models/jarvis/jarvis-high.onnx.json"
        
        try:
            self.voice = PiperVoice.load(self.model_path, config_path=self.config_path)
            print("Jarvis voice loaded successfully!")
        except Exception as e:
            print(f"WARNING: Could not load Jarvis voice: {e}")
            self.voice = None

    async def generate_audio(self, text: str) -> bytes:
        if not self.voice:
            return b""
        
        try:
            # Collect all audio chunks from Piper
            audio_chunks = []
            
            # Piper synthesize returns an iterator/generator of AudioChunk objects
            for chunk in self.voice.synthesize(text):
                # Each AudioChunk has audio_int16_bytes which contains the raw PCM audio
                audio_chunks.append(chunk.audio_int16_bytes)
            
            if not audio_chunks:
                return b""
            
            # Combine all chunks
            raw_audio = b''.join(audio_chunks)
            
            # Write to WAV format
            audio_io = io.BytesIO()
            with wave.open(audio_io, 'wb') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(22050)  # Piper's sample rate
                wav_file.writeframes(raw_audio)
            
            return audio_io.getvalue()
            
        except Exception as e:
            print(f"ERROR generating audio: {e}")
            return b""

tts_service = TTSService()

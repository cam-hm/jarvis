from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.app.services.websocket_manager import manager
from src.app.services.llm_service import llm_service
from src.app.services.tts_service import tts_service

app = FastAPI(title="Jarvis AI", description="A personal AI assistant", version="0.2.0")

# Mount static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def get():
    return FileResponse("src/static/index.html")

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        await manager.send_personal_message(f"Hello Mr. Stark. Systems online. Client ID: {client_id}", websocket)
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You said: {data}", websocket)
            
            # Send to Brain (LLM)
            response = await llm_service.generate_response(data)
            # Send Text Response first
            await manager.send_personal_message(response, websocket)
            
            # Stream Voice (TTS) - Sentence by sentence
            # Simple sentence splitting
            import re
            sentences = re.split(r'(?<=[.!?])\s+', response)
            
            for sentence in sentences:
                if sentence.strip():
                    # Generate audio for this sentence
                    audio_data = await tts_service.generate_audio(sentence)
                    if audio_data:
                        await websocket.send_bytes(audio_data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

@app.get("/health")
async def health_check():
    return {"status": "operational", "mode": "real-time"}

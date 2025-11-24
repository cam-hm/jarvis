# Jarvis AI - System Architecture

## 1. High-Level Architecture
The system follows a **Client-Server** architecture with **Real-time Event-Driven** communication.

```mermaid
graph TD
    User[Tony Stark] <-->|Audio/Video/Text| Client[Web Client (The Body)]
    Client <-->|WebSocket Stream| Server[FastAPI Backend (The Brain)]
    
    subgraph "The Brain (Server)"
        WS[WebSocket Manager]
        Orch[Orchestrator]
        
        subgraph "AI Modules"
            STT[Ear: Whisper]
            LLM[Mind: Gemini Flash]
            TTS[Mouth: Edge TTS]
            Vision[Eye: Gemini Vision]
        end
        
        WS <--> Orch
        Orch --> STT
        Orch --> Vision
        STT --> LLM
        Vision --> LLM
        LLM --> TTS
    end
```

## 2. Component Details

### A. Web Client (The Body)
- **Responsibility:** IO (Input/Output) and Rendering.
- **Components:**
    - **MediaManager:** Handles Mic & Camera access.
    - **SocketClient:** Manages WebSocket connection & binary data streaming.
    - **AvatarRenderer:** Three.js scene for the 3D character.
    - **AudioPlayer:** Queues and plays returned audio chunks.

### B. FastAPI Backend (The Brain)
- **Responsibility:** Processing and Intelligence.
- **Components:**
    - **ConnectionManager:** Handles multiple client connections (though primarily single-user).
    - **Pipeline:** An async processing chain:
        1.  `InputHandler`: Buffers incoming audio/video frames.
        2.  `STTService`: Transcribes audio buffer to text.
        3.  `BrainService`: Sends text + image context to LLM.
        4.  `TTSService`: Converts LLM response to audio.
    - **OutputHandler:** Streams audio + animation data back to client.

## 3. Data Flow (The Conversation Loop)

1.  **User Speaks:** Client captures audio -> Streams bytes to Server.
2.  **Server Listens:** Server buffers audio -> VAD (Voice Activity Detection) detects silence -> Triggers STT.
3.  **Server Thinks:** STT Text -> LLM (with System Prompt "You are Jarvis").
4.  **Server Responds:** LLM Stream -> TTS Stream -> Audio Bytes sent to Client.
5.  **Client Speaks:** Client receives Audio -> Plays Audio + Animates Avatar.

## 4. Directory Structure
```
jarvis_ai/
├── docs/               # Documentation
├── src/
│   ├── app/            # FastAPI App
│   │   ├── core/       # Config, Logging
│   │   ├── services/   # AI Services (LLM, STT, TTS)
│   │   ├── api/        # Routes & WebSocket Handlers
│   │   └── main.py     # Entry point
│   └── static/         # Frontend Assets (HTML, JS, Models)
├── tests/              # Tests
├── requirements.txt
└── README.md
```

# Jarvis AI - Project Requirements & Specifications

## 1. Project Overview
**Project Name:** Jarvis AI (Web Version)
**Goal:** Create a real-time, interactive AI avatar assistant that can communicate via voice and vision, running primarily on a web interface with a Python backend.
**Target Audience:** Tony Stark (The User) - Tech-savvy, appreciates premium aesthetics and high responsiveness.

## 2. Functional Requirements

### Phase 1: The Connection (Real-time Base)
- **FR-01:** System must support real-time bi-directional communication via WebSockets.
- **FR-02:** Web interface must allow users to connect/disconnect from the server.
- **FR-03:** Basic text chat interface for debugging and fallback.

### Phase 2: The Senses (Audio & Vision)
- **FR-04 (Hearing):** System must capture audio from the user's microphone and convert it to text (STT).
- **FR-05 (Speaking):** System must convert AI text responses to audio (TTS) and play it on the client.
- **FR-06 (Sight):** System must capture video frames from the user's webcam.
- **FR-07 (Perception):** System must analyze video frames to detect user presence and basic emotions.

### Phase 3: The Brain (Intelligence)
- **FR-08:** System must use an LLM to generate context-aware responses.
- **FR-09:** System must maintain conversation history (short-term memory).
- **FR-10:** System must be able to "see" and comment on what the user is doing/feeling based on visual input.

### Phase 4: The Face (Avatar)
- **FR-11:** Web interface must render a 3D or 2D avatar.
- **FR-12:** Avatar must sync lip movements (visemes) with the TTS audio.
- **FR-13:** Avatar must exhibit idle animations (blinking, looking around) to feel "alive".

## 3. Non-Functional Requirements
- **NFR-01 (Latency):** Audio-to-Audio response time should be minimized (Target: < 2 seconds).
- **NFR-02 (Cost):** Prioritize free/open-source technologies (Zero Cost architecture).
- **NFR-03 (Privacy):** Video/Audio data should be processed ephemerally and not stored permanently without permission.
- **NFR-04 (Aesthetics):** UI must be "Stark-level" premium (Dark mode, HUD elements, smooth animations).

## 4. Technology Stack (Zero Cost)
- **Frontend:** HTML5, Vanilla JS (or lightweight framework), Three.js (Avatar).
- **Backend:** Python FastAPI (Async).
- **Communication:** WebSockets.
- **AI Models:**
    - **LLM:** Google Gemini Flash 1.5 (API).
    - **STT:** Faster-Whisper (Local).
    - **TTS:** Edge-TTS (Free API).
    - **Vision:** Gemini Flash 1.5 (Multimodal capabilities).

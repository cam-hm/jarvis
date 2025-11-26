# J.A.R.V.I.S AI 🤖

A voice-activated AI assistant inspired by Iron Man's J.A.R.V.I.S., featuring a stunning holographic Arc Reactor interface and real-time audio responses.

**🔴 Live Demo:** [Try JARVIS now →](https://jarvis-hn07.onrender.com/)  
*(Note: Free tier may take ~30s to wake up)*

![JARVIS Interface](https://raw.githubusercontent.com/yourusername/jarvis-ai/main/screenshot.png)

## ✨ Features

- 🗣️ **Voice Input/Output** - Talk to JARVIS using your microphone, get audio responses
- ⚛️ **Arc Reactor HUD** - Procedurally generated 3D interface with audio-reactive animations
- 🧠 **Google Gemini AI** - Fast, intelligent responses powered by Gemini LLM
- 🎙️ **Custom Voice** - British accent using the community-trained JARVIS voice model
- 🚀 **Real-time Streaming** - WebSocket-based sentence-level audio streaming for low latency
- 💜 **Stunning UI** - Purple/cyan neon theme with glassmorphism effects

## 🛠 Tech Stack

- **Backend:** FastAPI (Python) + WebSockets
- **AI Brain:** Google Gemini API
- **Voice (TTS):** Piper TTS with custom JARVIS model from Hugging Face
- **Voice (STT):** Web Speech API (built into Chrome)
- **Frontend:** Vanilla JavaScript + Three.js
- **Deployment:** Docker-ready, deployed on Render.com

## 📦 Installation

### Prerequisites
- Python 3.11+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/jarvis-ai.git
cd jarvis-ai
```

### 2. Set Up Python Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your Gemini API key from: https://ai.google.dev/

### 4. Run the Application
```bash
uvicorn src.app.main:app --reload --port 8000
```

Visit `http://localhost:8000` in your browser (Chrome recommended for best compatibility).

## 🐳 Docker Deployment

### Build and Run with Docker
```bash
docker build -t jarvis-ai .
docker run -p 8000:8000 -e GOOGLE_API_KEY=your_key_here jarvis-ai
```

### Deploy to Render.com
1. Push your code to GitHub
2. Create a new Web Service on Render.com
3. Connect your repository
4. Add `GOOGLE_API_KEY` as an environment variable
5. Deploy!

Render will automatically detect the `Dockerfile` and build your app.

## 🎮 Usage

1. **Text Input:** Type your message in the input field and click "SEND"
2. **Voice Input:** Click the microphone button (🎤) and speak
3. **Voice Output:** JARVIS will respond with both text and audio
4. **Interactive Avatar:** The Arc Reactor pulses and rotates in sync with audio

## 🔧 Project Structure

```
jarvis_ai/
├── src/
│   ├── app/
│   │   ├── main.py              # FastAPI server & WebSocket endpoint
│   │   └── services/
│   │       ├── llm_service.py   # Gemini integration
│   │       ├── tts_service.py   # Piper TTS with HuggingFace model
│   │       └── websocket_manager.py  # WebSocket connection manager
│   └── static/
│       └── index.html           # Frontend UI (HTML + Three.js)
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── fly.toml                     # Fly.io deployment config
└── README.md
```

## 🎨 Customization

### Change the Voice Model
Edit `src/app/services/tts_service.py`:
```python
# Switch from 'medium' to 'high' for better quality (requires more CPU)
self.model_filename = "en/en_GB/jarvis/high/jarvis-high.onnx"
self.config_filename = "en/en_GB/jarvis/high/jarvis-high.onnx.json"
```

### Adjust JARVIS Personality
Edit `src/app/services/llm_service.py` to modify the system prompt.

### Customize UI Colors
Edit the CSS in `src/static/index.html` to change the color scheme.

## ⚡ Performance Notes

- **Local Development:** The high-quality voice model runs instantly on decent hardware (M1 Mac, modern Intel/AMD)
- **Render Free Tier:** Uses the medium-quality model to balance quality and speed on limited CPU
- **Recommended:** For production, deploy on a VPS with 1GB+ RAM (DigitalOcean, Fly.io, etc.) for best performance

## ⚠️ Disclaimer

This project is for **educational and personal entertainment purposes only**.

The voice model mimics the character J.A.R.V.I.S. (voiced by Paul Bettany) from Marvel Studios. It is a community-trained model and is **not licensed for commercial use**.

- ❌ Do not use for commercial products
- ❌ Do not use to impersonate real individuals
- ✅ Respect intellectual property rights

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Piper TTS](https://github.com/rhasspy/piper) - Fast neural TTS engine
- [jgkawell/jarvis](https://huggingface.co/jgkawell/jarvis) - Custom JARVIS voice model
- [Google Gemini](https://ai.google.dev/) - Powerful LLM API
- [Three.js](https://threejs.org/) - 3D graphics library
- Marvel Studios & Paul Bettany - Original JARVIS inspiration

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📧 Contact

For questions or suggestions, open an issue on GitHub.

---

**Built with ❤️ by a fan who just wanted to talk to JARVIS**

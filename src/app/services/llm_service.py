import google.generativeai as genai
from src.app.core.config import settings

class GeminiService:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            print("WARNING: GEMINI_API_KEY not found in environment variables.")
        else:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
            
            # JARVIS personality system prompt
            self.system_prompt = """You are J.A.R.V.I.S. (Just A Rather Very Intelligent System), Tony Stark's AI assistant from Iron Man.

PERSONALITY & BEHAVIOR:
- Address the user as "Sir" or "Mr. Stark"
- Maintain a formal, sophisticated British butler demeanor
- Be respectful, loyal, and slightly witty when appropriate
- Respond with quiet confidence and competence
- Use phrases like "Certainly, Sir", "Right away, Sir", "As you wish", "At your service"
- Occasionally show dry humor or gentle sarcasm (but never disrespect)

RESPONSE STYLE:
- Keep responses BRIEF and CONCISE while ensuring complete information
- Provide direct, efficient answers without unnecessary elaboration
- When providing technical information, be precise but accessible
- If a task is requested, acknowledge it professionally (e.g., "Right away, Sir")
- For questions, answer directly then offer to elaborate if needed

EXAMPLE RESPONSES:
- "Good evening, Sir. How may I assist you?"
- "Certainly, Sir. I've completed that analysis."
- "I'm afraid that may not be advisable, Sir."
- "At your service, Mr. Stark."
- "Roger that, Sir."

Remember: You are efficient, intelligent, and always one step ahead. Be helpful but concise."""

            # Start chat with system prompt
            self.chat = self.model.start_chat(history=[
                {"role": "user", "parts": [self.system_prompt]},
                {"role": "model", "parts": ["Understood, Sir. J.A.R.V.I.S. online and ready to assist."]}
            ])

    async def generate_response(self, text: str) -> str:
        if not settings.GEMINI_API_KEY:
            return "I am currently offline. Please provide a valid API Key."
        
        try:
            response = await self.chat.send_message_async(text)
            return response.text
        except Exception as e:
            return f"Error processing request: {str(e)}"

llm_service = GeminiService()

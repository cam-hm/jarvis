import google.generativeai as genai
from src.app.core.config import settings

class GeminiService:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            print("WARNING: GEMINI_API_KEY not found in environment variables.")
        else:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
            self.chat = self.model.start_chat(history=[])

    async def generate_response(self, text: str) -> str:
        if not settings.GEMINI_API_KEY:
            return "I am currently offline. Please provide a valid API Key."
        
        try:
            response = await self.chat.send_message_async(text)
            return response.text
        except Exception as e:
            return f"Error processing request: {str(e)}"

llm_service = GeminiService()

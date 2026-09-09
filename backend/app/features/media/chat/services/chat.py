import os

from fastapi import HTTPException
from google import genai


class GeminiChatService:
    def __init__(self):
        # Récupère ta clé API depuis ton fichier .env (ex: GEMINI_API_KEY)
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def generate_response(self, user_message: str) -> str:
        try:
            # On utilise le modèle standard et rapide gemini-2.5-flash (ou gemini-1.5-flash)
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Tu es l'assistant virtuel de l'école Nova School. Réponds de manière claire et utile à l'utilisateur.\n\nMessage : {user_message}",
            )
            return response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur avec l'IA Gemini : {str(e)}")



from app.common import httpx
from app.core.config import settings

from ..base import BaseNotificationService


class SMSProvider(BaseNotificationService):
    def __init__(self):
        # On récupère tes clés depuis settings
        self.api_key = settings.SMS_API_KEY
        self.api_url = settings.SMS_API_URL  # URL du fournisseur que tu choisiras
        self.sender_id = settings.SMS_SENDER_NAME  # Le nom qui s'affiche sur le téléphone

    async def send(self, recipient: str, message: str, **kwargs):
        """
        Envoi générique : C'est ici que tu brancheras l'API du fournisseur.
        """
        payload = {"to": recipient, "text": message, "from": self.sender_id}

        headers = {"Authorization": f"Bearer {self.api_key}"}

        # Simulation de l'appel API
        async with httpx.AsyncClient() as client:
            # response = await client.post(self.api_url, json=payload, headers=headers)
            # return response.status_code == 200
            print(f"SMS envoyé à {recipient} : {message}")
            return True

    async def send_code(self, phone: str, code: str):
        """
        Méthode spécifique pour tes codes OTP.
        """
        message = f"Babi Management : Votre code de vérification est {code}"
        return await self.send(phone, message)

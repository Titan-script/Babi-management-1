from app.common import httpx
from app.core import settings
from app.integrations.messaging.base import BaseNotificationService


class WhatsAppProvider(BaseNotificationService):
    def __init__(self):
        self.api_url = settings.WHATSAPP_API_URL
        self.api_token = settings.WHATSAPP_API_TOKEN

    async def send(self, recipient: str, message: str, **kwargs):
        payload = {"to": recipient, "type": "text", "text": {"body": message}}
        headers = {"Authorization": f"Bearer {self.api_token}"}

        async with httpx.AsyncClient() as client:
            response = await client.post(self.api_url, json=payload, headers=headers)
            return response.status_code == 200

    async def send_code(self, phone: str, code: str):
        message = f"Babi Management : Votre code de validation est {code}"
        return await self.send(phone, message)

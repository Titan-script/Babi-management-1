from app.common import httpx
from app.core import settings
from app.integrations.messaging.base import BaseNotificationService


class TelegramProvider(BaseNotificationService):
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    async def send(self, recipient: str, message: str, **kwargs):
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": recipient, "text": message, "parse_mode": "HTML"}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            return response.status_code == 200

    async def send_code(self, chat_id: str, code: str):
        message = f"<b>Babi Management</b>\nVotre code de validation est : <code>{code}</code>"
        return await self.send(chat_id, message)

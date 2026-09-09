from app.common import (
    json,
    time,
)
from app.infrastructure import redis_config

from .otp_service import OTPService
from .providers.email import EmailProvider
from .providers.sms import SMSProvider
from .providers.telegram import TelegramProvider
from .providers.whatsapp import WhatsAppProvider


class MessagingManager:
    def __init__(self):
        self.providers = {
            "email": EmailProvider(),
            "sms": SMSProvider(),
            "telegram": TelegramProvider(),
            "whatsapp": WhatsAppProvider(),
        }

    async def send_otp_code(self, channel: str, target: str):
        code = OTPService.generate()
        created_at = time.time()

        # Stockage sécurisé dans Redis (TTL 5 minutes)
        otp_data = {"code": code, "created_at": created_at}
        redis_config.setex(f"otp:{target}", 300, json.dumps(otp_data))

        provider = self.providers.get(channel)
        if not provider:
            raise ValueError(f"Canal {channel} non supporté")
        return await provider.send_code(target, code)

    async def send_alert(self, channel: str, target: str, message: str, **kwargs):
        provider = self.providers.get(channel)
        if not provider:
            raise ValueError(f"Canal {channel} non supporté")
        return await provider.send(target, message, **kwargs)

    async def verify_code(self, target: str, provided_code: str) -> bool:
        raw_data = redis_config.get(f"otp:{target}")
        if not raw_data:
            return False

        data = json.loads(raw_data)
        if not data or OTPService.is_expired(data["created_at"]):
            return False

        is_valid = OTPService.verify(data["code"], provided_code)
        if is_valid:
            # Suppression du code après validation réussie (usage unique)
            redis_client.delete(f"otp:{target}")

        return is_valid


messaging_manager = MessagingManager()

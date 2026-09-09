from app.common import credentials, firebase_admin, messaging
from app.core.config import settings


class PushProvider:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_P)
            firebase_admin.initialize_app(cred)

    async def send(self, token: str, title: str, body: str, **kwargs):
        message = messaging.Message(
            notification=messaging.Notification(title=title, body=body),
            token=token,
            data=kwargs.get("data", {}),
        )
        try:
            response = messaging.send(message)
            return True, response
        except Exception as e:
            return False, str(e)

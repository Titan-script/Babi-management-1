from .models import NotificationHistory
from .providers.push import PushProvider


class NotificationManager:
    def __init__(self, db_session):
        self.push = PushProvider()
        self.db = db_session

    async def notify_user(
        self, user_id: int, title: str, body: str, channels: list = None, type: str = "info"
    ):
        from app.api import NotifyWebSocketManager as ws_manager

        # 1. Enregistrement en BDD
        new_notif = NotificationHistory(
            user_id=user_id, title=title, message=body, type=type, is_read=False
        )
        self.db.add(new_notif)
        await self.db.commit()
        await self.db.refresh(new_notif)

        channels = channels or ["ws", "push"]

        # 2. Exécution des canaux
        if "ws" in channels:
            await ws_manager.send_personal_message(f"{title}: {body}", user_id)

        if "push" in channels:
            # Récupération du token depuis l'utilisateur si disponible
            token = getattr(new_notif.user, "fcm_token", None) if new_notif.user else None
            if token:
                await self.push_provider.send(token, title, body)

        return new_notif

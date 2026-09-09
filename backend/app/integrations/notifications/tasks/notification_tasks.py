from app.common import asyncio
from app.tasks import celery_app

from ..manager import NotificationManager


@celery_app.task(name="tasks.notifications.send")
def task_send_push_notification(user_id: int, title: str, body: str, channels: list, type: str):
    from app.db import AsyncSessionLocal

    """Tâche Celery pour l'envoi asynchrone des notifications."""

    async def _run():
        async with AsyncSessionLocal() as session:
            manager = NotificationManager(session)
            return await manager.notify_user(user_id, title, body, channels, type)

    return asyncio.run(_run())

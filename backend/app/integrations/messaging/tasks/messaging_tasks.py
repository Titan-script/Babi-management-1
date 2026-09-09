from app.common import asyncio
from app.tasks.celery_config import celery_app

from ..manager import messaging_manager


@celery_app.task(name="tasks.messaging.alert")
def task_send_alert(channel: str, target: str, message: str):
    """Tâche Celery pour l'envoi d'alertes asynchrones."""
    return asyncio.run(messaging_manager.send_alert(channel, target, message))


@celery_app.task(name="tasks.messaging.otp", bind=True, max_retries=3)
def task_send_otp(self, channel: str, target: str):
    """Tâche Celery pour l'envoi de codes OTP avec gestion des retries en cas d'échec."""
    try:
        return asyncio.run(messaging_manager.send_otp_code(channel, target))
    except Exception as exc:
        # Réessaie la tâche après 60 secondes en cas d'erreur de l'API tierce
        raise self.retry(exc=exc, countdown=60)

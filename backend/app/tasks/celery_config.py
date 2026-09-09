from celery import Celery

from app.core import settings

celery_app = Celery(
    "nova_tasks",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=[
        "app.integrations.messaging.tasks.notification_tasks",
    ],
)

# Configuration optionnelle pour optimiser le comportement de Celery
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

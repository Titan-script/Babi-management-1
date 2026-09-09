from app.common import wraps

from .tasks.notification_tasks import task_send_push_notification

MESSAGES = {
    "create": {"title": "Succès", "body": "Création effectuée avec succès."},
    "update": {"title": "Mise à jour", "body": "Modification enregistrée."},
    "delete": {"title": "Suppression", "body": "Élément supprimé."},
}


def notify_after(action_key: str, channels: list = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)

            if result and hasattr(result, "user_id"):
                msg = MESSAGES.get(action_key, {"title": "Notification", "body": "Action réalisée"})
                task_send_push_notification.delay(
                    user_id=result.user_id,
                    title=msg["title"],
                    body=msg["body"],
                    channels=channels or ["ws", "push"],
                    type=action_key,
                )
            return result

        return wrapper

    return decorator

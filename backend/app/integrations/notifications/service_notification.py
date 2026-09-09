from .tasks.notification_tasks import task_send_push_notification


class NotificationService:
    @staticmethod
    def notify_user_async(user_id: int, title: str, body: str, channels: list, type: str):
        """
        Déclenche l'envoi de notifications (Push, Email, SMS...) en arrière-plan via Celery
        sans bloquer l'exécution de ton application.
        """
        return task_send_push_notification.delay(
            user_id=user_id, title=title, body=body, channels=channels, type=type
        )

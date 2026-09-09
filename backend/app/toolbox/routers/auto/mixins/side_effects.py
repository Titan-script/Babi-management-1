from app.common import Any


class SideEffectsMixin:
    async def _trigger_side_effects(self, instance: Any, event_type: str):
        """Déclenche les tâches post-commit (notifications)."""
        if not hasattr(instance, "id"):
            return

        if event_type in self.notification_config and hasattr(
            self.model_crud, "trigger_post_commit_task"
        ):
            config = self.notification_config.get(event_type, {})
            user_id = getattr(instance, "user_id", None)
            if user_id:
                self.model_crud.trigger_post_commit_task(
                    task_name="notification",
                    user_id=user_id,
                    title=config.get("title", "Notification Babi Management"),
                    body=config.get("body", "Une mise à jour a eu lieu sur votre compte."),
                    channels=config.get("channels", ["push"]),
                    type=event_type,
                )

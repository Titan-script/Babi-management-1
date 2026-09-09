from app.common import Any


class SideEffectsMixin:
    async def _trigger_push_notification(
        self, manager_instance: Any, action_name: str, result: Any, config: dict
    ):
        crud = getattr(manager_instance, "crud", None) or manager_instance
        if hasattr(crud, "trigger_post_commit_task"):
            user_id = getattr(result, "user_id", None) or getattr(result, "id", None)
            if user_id:
                await crud.trigger_post_commit_task(
                    task_name="notification",
                    user_id=user_id,
                    title=config.get("title", "Notification Babi Management"),
                    body=config.get("body", "Action effectuée avec succès."),
                    channels=["push"],
                    type=action_name,
                )

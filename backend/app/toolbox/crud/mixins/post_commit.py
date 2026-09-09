from app.common import event
from app.integrations import IdentityService, NotificationService


class PostCommitMixin:
    def trigger_post_commit_task(self, task_name: str, **task_kwargs):
        if not self.db:
            return

        def run_task(session_obj):
            if task_name == "notification":
                NotificationService.notify_user_async(**task_kwargs)
            elif task_name == "alert":
                NotificationService.send_alert_async(**task_kwargs)
            elif task_name == "otp":
                NotificationService.send_otp_async(**task_kwargs)
            elif task_name == "identity_tags":
                instance = task_kwargs.get("instance")
                if instance:
                    IdentityService.trigger_tags_if_enabled(instance)

        event.listen(self.db, "after_commit", run_task, once=True)

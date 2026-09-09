"""
from app.core.deps import get_db
"""


class WrappedEndpointMixin:
    async def wrapped_endpoint(*args, **kwargs):

        manager_instance = self.manager_cls if callable(self.manager_cls) else self.manager_cls

        if not hasattr(manager_instance, action_name):
            raise AttributeError(
                f"Le manager '{manager_instance.__class__.__name__}' ne possède pas la méthode '{action_name}'."
            )

        func = getattr(manager_instance, action_name)
        result = await func(*args, **kwargs) if callable(func) else func

        notif_config = self.notification_config.get(action_name, {})
        if notif_config:
            await self._trigger_push_notification(
                manager_instance, action_name, result, notif_config
            )

        return result

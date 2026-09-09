from app.common import (
    APIRouter,
    List,
    Optional,
    Type,
    TypeVar,
)

from .mixins.crud_routes import CrudRoutersMixin
from .mixins.deps import DepsMixin
from .mixins.side_effects import SideEffectsMixin
from .mixins.wrapped import WrappedEndpointMixin

# 1. Tu définis ta TypeVar pour le manager
ManagerType = TypeVar("ManagerType")


class ManuelRouter(DepsMixin, SideEffectsMixin, CrudRoutersMixin, WrappedEndpointMixin):
    def __init__(
        self,
        manager_cls: Type[ManagerType],
        prefix: str = "",
        tags: Optional[List[str]] = None,
        notification_config: Optional[dict] = None,
        required_feature: Optional[str] = None,
    ):

        self.manager_cls: Type[ManagerType] = manager_cls
        self.router = APIRouter(prefix=prefix, tags=tags or [])
        self.notification_config = notification_config or {}
        self.resource = prefix.strip("/").replace("/", "_") if prefix else "default"
        self.required_feature = required_feature

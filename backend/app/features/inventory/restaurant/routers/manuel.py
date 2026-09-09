from fastapi import APIRouter

from app.common import STATUS

from ..managers.main import RestaurantManager
from ..schemas.restaurant import (
    OrderCreate,
)

# ============================MANUAL ROUTERS======================================


POST = "POST"
STATUS = STATUS.OK


def get_order_manual_router() -> APIRouter:
    from app.common import FEATURES, PREFIX
    from app.toolbox import ManagerFactory, ManuelRouter

    FEATURES = FEATURES.INVENTORY
    PREFIX = f"{PREFIX.INVENTORY}/restaurant"
    TAGS = ["Order Restaurant"]

    MANAGER = ManagerFactory.get_manager(RestaurantManager)
    manual_router = ManuelRouter(
        manager_cls=MANAGER, prefix=PREFIX, tags=TAGS, required_feature=FEATURES
    )
    P = "/register"
    manual_router.add(path=P, method=POST, action_name="create_order", response_model=OrderCreate)

    return manual_router.router


manuel_routers = [
    get_order_manual_router,
]

from fastapi import APIRouter

from app.common import STATUS

from ..managers.main import InventoryManager
from ..schemas.stock import (
    INVStockAdjustmentCreate,
    INVStockOutputCreate,
    INVStockReceptionCreate,
)

# ==============================MANUAL ROUTERS ======================================

POST = "POST"
STATUS = STATUS.OK


def get_inventory_manual_router() -> APIRouter:
    from app.common import FEATURES, PREFIX
    from app.toolbox import ManagerFactory, ManuelRouter

    FEATURES = FEATURES.INVENTORY
    PREFIX = f"{PREFIX.INVENTORY}/gestion"
    TAGS = ["Gestion Stocks"]

    MANAGER = ManagerFactory.get_manager(InventoryManager)
    manual_router = ManuelRouter(
        manager_cls=MANAGER, prefix=PREFIX, tags=TAGS, required_feature=FEATURES
    )
    P = "/receive"
    manual_router.add(
        path=P,
        method=POST,
        action_name="receive_stock",
        response_model=INVStockReceptionCreate,
    )
    P = "/output"

    manual_router.add(
        path=P,
        method=POST,
        action_name="register_output",
        status_code=STATUS,
        response_model=INVStockOutputCreate,
    )
    P = "/adjust"
    manual_router.add(
        path=P,
        method=POST,
        action_name="adjust_stock",
        status_code=STATUS,
        response_model=INVStockAdjustmentCreate,
    )

    return manual_router.router


manuel_routers = [
    get_inventory_manual_router,
]

from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.restaurant import Order
from ..schemas.restaurant import (
    OrderRead,
    OrderUpdate,
)

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================

FEATURES = FEATURES.INVENTORY
PREFIX = PREFIX.INVENTORY
STATUS = STATUS.OK
POST = "POST"


# --- ROUTEUR CATEGORIES ---
def get_restaurant_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Order)
    TAGS = ["Order Restaurant"]
    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_update=OrderRead,
        schema_read=OrderUpdate,
        prefix=f"{PREFIX}/restaurant",
        tags=TAGS,
        required_feature=FEATURES,
    ).router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

restaurant_routers = [
    get_restaurant_auto_router,
]

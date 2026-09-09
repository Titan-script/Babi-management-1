from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.ai import Chat, Product, Variant
from ..schemas.catalog import (
    INVChatCreate,
    INVChatRead,
    INVChatUpdate,

)

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================

FEATURES = FEATURES.INVENTORY
PREFIX = PREFIX.INVENTORY
STATUS = STATUS.OK
POST = "POST"


# --- ROUTEUR CATEGORIES ---
def get_chat_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Chat)
    TAGS = ["Inventory Categories"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_update=INVChatRead,
        schema_read=INVChatUpdate,
        prefix=f"{PREFIX}/categories",
        tags=TAGS,
        required_feature=FEATURES,
    ).router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

catalog_routers = [
    get_chat_auto_router,
    get_product_auto_router,
    get_variant_auto_router,
]

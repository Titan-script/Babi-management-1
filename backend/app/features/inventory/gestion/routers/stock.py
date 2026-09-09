from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.stock import Stock, StockHistory
from ..schemas.stock import (
    INVStockHistoryRead,
    INVStockRead,
)

# =====================================================================
#  AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================

PREFIX = PREFIX.INVENTORY
FEATURES = FEATURES.INVENTORY
STATUS = STATUS.OK


def get_gestion_stocks_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Stock)
    TAGS = ["State Stocks"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=INVStockRead,
        prefix=f"{PREFIX}/gestion",
        tags=TAGS,
        allow_export=True,
        required_feature=FEATURES,
    ).router


def get_gestion_history_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(StockHistory)
    TAGS = ["History Stocks"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=INVStockHistoryRead,
        prefix="/gestion/history",
        tags=TAGS,
        allow_export=True,
        required_feature=FEATURES,
    ).router


# =====================================================================
# 3. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

gestions_routers = [
    get_gestion_stocks_auto_router,
    get_gestion_history_auto_router,
]

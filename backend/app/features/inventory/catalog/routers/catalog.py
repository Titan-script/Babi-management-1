from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.catalog import Category, Product, Variant
from ..schemas.catalog import (
    INVCategoryCreate,
    INVCategoryRead,
    INVCategoryUpdate,
    INVProductCreate,
    INVProductRead,
    INVProductUpdate,
    INVVariantCreate,
    INVVariantRead,
    INVVariantUpdate,
)

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================

FEATURES = FEATURES.INVENTORY
PREFIX = PREFIX.INVENTORY
STATUS = STATUS.OK
POST = "POST"


# --- ROUTEUR CATEGORIES ---
def get_category_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Category)
    TAGS = ["Inventory Categories"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_create=INVCategoryCreate,
        schema_update=INVCategoryRead,
        schema_read=INVCategoryUpdate,
        prefix=f"{PREFIX}/categories",
        tags=TAGS,
        required_feature=FEATURES,
    ).router


# --- ROUTEUR PRODUCTS ---
def get_product_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Product)
    TAGS = ["Inventory Products"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_create=INVProductCreate,
        schema_read=INVProductRead,
        schema_update=INVProductUpdate,
        prefix=f"{PREFIX}/products",
        tags=TAGS,
        required_feature=FEATURES,
    ).router


# --- ROUTEUR VARIANTS ---
def get_variant_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(Variant)
    TAGS = ["Inventory Variants"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_create=INVVariantCreate,
        schema_read=INVVariantRead,
        schema_update=INVVariantUpdate,
        prefix=f"{PREFIX}/catalogs",
        tags=TAGS,
        unique_fields=["sku"],
        required_feature=FEATURES,
    ).router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

catalog_routers = [
    get_category_auto_router,
    get_product_auto_router,
    get_variant_auto_router,
]

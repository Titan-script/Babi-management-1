from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.infos import OrgInfos

# --- Modèles et Schémas ---
from ..schemas.infos import OrgInfosRead, OrgInfosUpdate

# =================TAG COMMON=================
PREFIX = PREFIX.ORG_IDENTITY
FEATURES = FEATURES.ORG_IDENTITY
STATUS = STATUS.OK

# ============================AUTO ROUTERS ==================================


def get_tenant_auto_router() -> APIRouter:

    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(OrgInfos)
    TAGS = ["Tenant Infos"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_update=OrgInfosUpdate,
        schema_read=OrgInfosRead,
        prefix=f"{PREFIX}/tenant",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=True,
    ).router


# =====================================================================
# LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

identity_tenant_routers = [
    get_tenant_auto_router,
]

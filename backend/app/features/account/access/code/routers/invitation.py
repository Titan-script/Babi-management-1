from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.invitation import InvitationCode
from ..schemas.invitation import InvitationCodeRead

# =================TAG COMMON=================
PREFIX = PREFIX.ACCOUNT_ACCESS
FEATURES = FEATURES.ACCOUNT_ACCESS
STATUS = STATUS.OK

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================


def get_invitation_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(InvitationCode)
    TAGS = ["INVITATION"]
    autorouter = AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=InvitationCodeRead,
        prefix=f"{PREFIX}/invitation",
        tags=TAGS,
        unique_fields=["code"],
        required_feature=FEATURES,
        allow_export=True,
    )
    return autorouter.router


# =====================================================================
# 3. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

invitation_routers = [
    get_invitation_auto_router,
]

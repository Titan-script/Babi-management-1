from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ...user.models.infos import UserInfos
from ..schemas.admin import ProfileAdminRead, ProfileAdminUpdate

# =================TAG COMMON=================
PREFIX = PREFIX.ACCOUNT_IDENTITY
FEATURES = FEATURES.ACCOUNT_IDENTITY
STATUS = STATUS.OK


def get_admin_auth_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    TAGS = ["Identity-Admin"]
    MODELE_SQL = BaseCrud(UserInfos)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=ProfileAdminRead,
        schema_update=ProfileAdminUpdate,
        prefix=f"{PREFIX}/admin",
        tags=TAGS,
        required_feature=FEATURES,
        allow_me=True,
    ).router


profil_admin_routers = [
    get_admin_auth_auto_router,
]

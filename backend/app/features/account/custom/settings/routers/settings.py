from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS
from app.toolbox import AutoRouter, BaseCrud

from ..models.settings import UserSetting
from ..schemas.settings import UserSettingRead, UserSettingUpdate

# =================TAG COMMON=================
PREFIX = PREFIX.ACCOUNT_CUSTOM
FEATURES = FEATURES.ACCOUNT_CUSTOM
STATUS = STATUS.OK


def user_settings_auto_router() -> APIRouter:
    TAGS = ["User-Settings"]

    return AutoRouter(
        model_crud=BaseCrud(UserSetting),
        schema_read=UserSettingRead,
        schema_update=UserSettingUpdate,
        prefix=f"{PREFIX}/settings",
        tags=TAGS,
        allow_me=True,
        required_feature=FEATURES,
    ).router


# Liste groupée à importer dans ton fichier global `all_routers`
custom_settings_routers = [
    user_settings_auto_router,
]

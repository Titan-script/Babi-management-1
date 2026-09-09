from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.preference import UserPreference
from ..schemas.preference import UserPreferenceRead, UserPreferenceUpdate

# =================TAG COMMON=================
PREFIX = PREFIX.ACCOUNT_CUSTOM
FEATURES = FEATURES.ACCOUNT_CUSTOM
STATUS = STATUS.OK


def get_user_preferences_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    TAGS = ["User-Preferences"]
    return AutoRouter(
        model_crud=BaseCrud(UserPreference),
        schema_read=UserPreferenceRead,
        schema_update=UserPreferenceUpdate,
        prefix=f"{PREFIX}/preferences",
        tags=TAGS,
        allow_me=True,
    ).router


custom_preference_routers = [
    get_user_preferences_auto_router,
]

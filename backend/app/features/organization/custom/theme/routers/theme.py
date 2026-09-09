from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.theme import OrgTheme
from ..schemas.theme import OrgThemeRead, OrgThemeUpdate

# =================TAG COMMON=================
TAGS = ["Org Themes"]
PREFIX = PREFIX.ORG_CUSTOM
FEATURES = FEATURES.ORG_CUSTOM
STATUS = STATUS.OK


#  Thèmes d'customanisations (AutoRouter)
def get_theme_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    MODELE_SQL = BaseCrud(OrgTheme)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=OrgThemeRead,
        schema_update=OrgThemeUpdate,
        prefix=f"{PREFIX}/themes",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=False,
    ).router


custom_theme_routers = [
    get_theme_auto_router,
]

"""from fastapi import APIRouter, status

from ...settings.schemas.security_settings import (
    SecuSetSecretCreate,SecuVerifySecretCreate
)

def get_settings_manuel_router() -> APIRouter:
    from app.toolbox import ManagerFactory,ManuelRouter
    from ..managers.main import SettingsManager
    from app.common import PREFIX, TAGS, FEATURES, STATUS

    TAGS=TAGS.AUTH_LOGIN
    FEATURES=FEATURES.AUTH_LOGIN
    PREFIX=PREFIX.AUTH_LOGIN
    STATUS=STATUS.OK
    POST="POST"

    MANAGER = ManagerFactory.get_manager(SettingsManager)
    manual_router = ManuelRouter( manager_cls=MANAGER,prefix=PREFIX,tags=TAGS,required_feature=FEATURES  )

    PATH="/secret-question/initiate"
    manual_router.add(
        path=PATH,method=POST,
        action_name="set_secret_question",status_code=STATUS,
        response_model=SecuSetSecretCreate
    )

    PATH="/secret-question/confirm"
    manual_router.add(
        path=PATH,method=POST,
        action_name="verify_secret_answer",status_code=STATUS,
        response_model=SecuVerifySecretCreate
    )
    return manual_router.router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

manuel_routers = [
    get_settings_manuel_router,
]


"""

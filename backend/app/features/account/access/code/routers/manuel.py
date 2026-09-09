from fastapi import APIRouter

from ...code.schemas.invitation import InvitationCodeCreate


def get_code_manuel_router() -> APIRouter:
    from app.common import FEATURES, PREFIX, STATUS
    from app.toolbox import ManagerFactory, ManuelRouter

    from ..managers.main import InvitationCodeManager

    TAGS = ["INVITATION"]
    FEATURES = FEATURES.ACCOUNT_ACCESS
    STATUS = STATUS.OK
    POST = "POST"
    PREFIX = f"{PREFIX.ACCOUNT_ACCESS}/invitations"

    MANAGER = ManagerFactory.get_manager(InvitationCodeManager)
    manual_router = ManuelRouter(
        manager_cls=MANAGER, prefix=PREFIX, tags=TAGS, required_feature=FEATURES
    )

    PATH = "/generate"
    manual_router.add(
        path=PATH,
        method=POST,
        action_name="create_invitation_code",
        response_model=InvitationCodeCreate,
    )

    return manual_router.router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

manuel_routers = [
    get_code_manuel_router,
]

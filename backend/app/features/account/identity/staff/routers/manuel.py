from fastapi import APIRouter

from ..schemas.staff import UserStaffCreate


def get_auth_staff_manuel_router() -> APIRouter:
    from app.common import FEATURES, PREFIX, STATUS
    from app.toolbox import ManagerFactory, ManuelRouter

    from ..managers.main import StaffManager

    TAGS = ["Identity-Staff"]
    FEATURES = FEATURES.ACCOUNT_IDENTITY
    PREFIX = f"{PREFIX.ACCOUNT_IDENTITY}/staff"
    STATUS = STATUS.OK
    POST = "POST"

    MANAGER = ManagerFactory.get_manager(StaffManager)

    manual_router = ManuelRouter(
        manager_cls=MANAGER, prefix=PREFIX, tags=TAGS, required_feature=FEATURES
    )

    PATH = "/register"
    manual_router.add(
        path=PATH,
        method=POST,
        action_name="register_staff",
        response_model=UserStaffCreate,
    )

    return manual_router.router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

manuel_routers = [
    get_auth_staff_manuel_router,
]

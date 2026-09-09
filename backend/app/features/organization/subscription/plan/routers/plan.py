from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.plan import OrgPlanSubscription
from ..schemas.plan import (
    OrgPlanSubscriptionCreate,
    OrgPlanSubscriptionRead,
    OrgPlanSubscriptionUpdate,
)

# =================TAG COMMON=================
PREFIX = PREFIX.ORG_SUBSCRIPTION
FEATURES = FEATURES.ORG_SUBSCRIPTION
STATUS = STATUS.OK

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================


def get_subscription_plan_auto_router() -> APIRouter:

    from app.toolbox import AutoRouter, BaseCrud

    TAGS = ["Subscription Plans"]
    MODELE_SQL = BaseCrud(OrgPlanSubscription)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_create=OrgPlanSubscriptionCreate,
        schema_update=OrgPlanSubscriptionUpdate,
        schema_read=OrgPlanSubscriptionRead,
        prefix=f"{PREFIX}/plan",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=True,
        allow_import=False,
    ).router


subscription_plan_routers = [get_subscription_plan_auto_router]

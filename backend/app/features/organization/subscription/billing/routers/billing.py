from fastapi import APIRouter

from app.common import FEATURES, PREFIX, STATUS

from ..models.billing import OrgBilling
from ..schemas.billing import (
    OrgBillingCreate,
    OrgBillingRead,
)

# =================TAG COMMON=================
PREFIX = PREFIX.ORG_SUBSCRIPTION
FEATURES = FEATURES.ORG_SUBSCRIPTION
STATUS = STATUS.OK

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================


def get_subscription_billing_auto_router() -> APIRouter:
    from app.toolbox import AutoRouter, BaseCrud

    TAGS = ["Subscription-Billing"]
    MODELE_SQL = BaseCrud(OrgBilling)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_create=OrgBillingCreate,
        schema_read=OrgBillingRead,
        prefix=f"{PREFIX}/billings",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=True,
        allow_import=False,
    ).router


subscription_billing_routers = [
    get_subscription_billing_auto_router,
]

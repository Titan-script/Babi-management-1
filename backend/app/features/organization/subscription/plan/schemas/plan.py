from typing import List, Optional

from app.toolbox import BaseReadSchema, BaseSchema

# ==================== SUBSCRIPTION SCHEMAS ====================
# OrgPlanSubscriptionCreate,OrgPlanSubscriptionRead,OrgPlanSubscriptionUpdate


class OrgPlanSubscriptionBase(BaseSchema):
    name: str
    features: str  # ex: "bus,stock,sms"
    days_duration: int


class OrgPlanSubscriptionCreate(OrgPlanSubscriptionBase):
    pass


class OrgPlanSubscriptionUpdate(BaseSchema):
    name: Optional[str] = None
    features: Optional[str] = None
    days_duration: Optional[int] = None


class OrgPlanSubscriptionRead(OrgPlanSubscriptionBase, BaseReadSchema):
    features_list: List[str]


class OrgPlanSubscriptionNested(OrgPlanSubscriptionBase, BaseReadSchema):
    pass

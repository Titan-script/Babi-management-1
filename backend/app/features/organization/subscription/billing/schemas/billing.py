from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field

from app.toolbox import BaseReadSchema, BaseSchema

from ...plan.schemas.plan import OrgPlanSubscriptionNested

# ==================== SUBSCRIPTION SCHEMAS ====================


class BillingCycle(str, Enum):
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class OrgBillingBase(BaseSchema):
    billing_cycle: "BillingCycle" = Field(default=BillingCycle.MONTHLY)


class OrgBillingCreate(OrgBillingBase):
    plan_id: int


class OrgBillingRead(OrgBillingBase, BaseReadSchema):
    plan: Optional["OrgPlanSubscriptionNested"]
    start_date: datetime
    end_date: datetime


class OrgBillingNested(OrgBillingBase, BaseReadSchema):
    plan: Optional["OrgPlanSubscriptionNested"]
    start_date: datetime
    end_date: datetime

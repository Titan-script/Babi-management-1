from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import BaseTenant

# ==================== ABONNEMENTS & PLANS ====================


class BillingCycle(str, Enum):
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class OrgBilling(BaseTenant, table=True):
    __tablename__ = "org_subscriptions"

    plan_id: int = Field(foreign_key="subscription_plans.id")

    # 2. Utilise l'Enum comme type de champ
    billing_cycle: BillingCycle = Field(default=BillingCycle.MONTHLY)
    start_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_date: datetime
    is_active: bool = Field(default=True)

    org: Optional["Organization"] = Relationship(back_populates="subscription")
    plan: Optional["SubscriptionPlan"] = Relationship()

    @property
    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.end_date

    def set_end_date_from_plan(self, plan):
        """Calcule automatiquement la end_date selon le plan et le cycle choisi."""
        multiplier = 12 if self.billing_cycle == BillingCycle.YEARLY else 1
        total_days = plan.days_duration * multiplier
        if self.billing_cycle == BillingCycle.YEARLY:
            total_days = 365

        self.end_date = self.start_date + timedelta(days=total_days)

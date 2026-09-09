from typing import List

from app.toolbox import BaseTenant


class OrgPlanSubscription(BaseTenant, table=True):
    __tablename__ = "subscription_plans"

    name: str
    features: str = ""  # Ex: "inventory_management,school_transport,dormitory_access"
    days_duration: int = 30

    @property
    def features_list(self) -> List[str]:
        if not self.features:
            return []
        return [f.strip() for f in self.features.split(",")]

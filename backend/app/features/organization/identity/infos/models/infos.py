from typing import List, Optional
from uuid import uuid4

from sqlmodel import Field, Relationship

from app.toolbox import BaseOrg, ImageAssetMixin, NfcAssetMixin, QRCodeAssetMixin

# ==================== ORGANISATION ====================


class OrgInfos(BaseOrg, NfcAssetMixin, QRCodeAssetMixin, ImageAssetMixin, table=True):
    __tablename__ = "organizations"

    id: Optional[int] = Field(default=None, primary_key=True)
    unique_slug: str = Field(unique=True, index=True)
    display_name: str
    owner_name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    is_blocked: bool = Field(default=False)

    portal_token: str = Field(default_factory=lambda: uuid4().hex, index=True)

    subscription: "OrgBilling" = Relationship(
        back_populates="org", sa_relationship_kwargs={"uselist": False}
    )
    theme: Optional["OrgTheme"] = Relationship(
        back_populates="org", sa_relationship_kwargs={"uselist": False}
    )
    settings: Optional["OrgSettings"] = Relationship(
        back_populates="org", sa_relationship_kwargs={"uselist": False}
    )
    user: List["UserInfos"] = Relationship(
        back_populates="org", sa_relationship_kwargs={"uselist": False}
    )

    def has_feature(self, feature_name: str) -> bool:
        """Vérifie si l'organisation possède la feature via son abonnement actif."""
        if self.is_blocked:
            return False

        if not self.subscription or not self.subscription.is_active or self.subscription.is_expired:
            return False

        plan = self.subscription.plan
        if not plan:
            return False

        return feature_name in plan.features_list

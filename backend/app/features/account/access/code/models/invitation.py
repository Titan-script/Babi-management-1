from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import ApprovalMixin, BaseTenant, ExpiryMixin, UsageTrackerMixin


class InvitationCode(BaseTenant, ApprovalMixin, ExpiryMixin, UsageTrackerMixin, table=True):
    __tablename__ = "invitation_codes"
    code: str = Field(unique=True, index=True)
    target_role: str
    purpose: str = Field(default="RECRUITMENT")

    user: Optional["UserInfos"] = Relationship(back_populates="invitation_code")

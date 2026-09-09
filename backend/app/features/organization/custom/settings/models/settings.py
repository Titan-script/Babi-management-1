from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import BaseTenant


class OrgSettings(BaseTenant, table=True):
    __tablename__ = "org_settings"

    sms_balance: int = Field(default=0)
    is_setup_completed: bool = Field(default=False)

    org: Optional["Organization"] = Relationship(back_populates="settings")

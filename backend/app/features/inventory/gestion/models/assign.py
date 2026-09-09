from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import BaseTenant


# --- Store Keeper ---
class ProfileStoreKeeper(BaseTenant, table=True):
    __tablename__ = "store_keepers"
    user_id: int = Field(foreign_key="users.id")
    can_approve_requests: bool = Field(default=True)

    user: Optional["UserInfos"] = Relationship(back_populates="storekeeper_profile")

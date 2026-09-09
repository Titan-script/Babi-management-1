from app.common import JSON, Column, Field, Optional, Relationship
from app.toolbox import BaseTenant


class NotificationHistory(BaseTenant, table=True):
    __tablename__ = "notifications"

    title: str = Field(nullable=False)
    message: str = Field(nullable=False)
    type: str = Field(default="info", index=True)
    is_read: bool = Field(default=False, index=True)
    action_url: Optional[str] = Field(default=None)
    payload: Optional[dict] = Field(default=None, sa_column=Column(JSON))

    user_id: int = Field(foreign_key="users.id", index=True)
    user: Optional["UserInfos"] = Relationship(back_populates="notifications")

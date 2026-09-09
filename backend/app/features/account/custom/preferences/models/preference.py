from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class UserPreference(SQLModel, table=True):
    __tablename__ = "user_preference"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True, index=True)

    # Confort & Interface
    theme: str = Field(default="system")  # "light", "dark", "system"
    language: str = Field(default="fr")  # "fr", "en"
    push_notifications_enabled: bool = Field(default=True)
    email_notifications_enabled: bool = Field(default=True)

    user: Optional["User"] = Relationship(back_populates="preferences")

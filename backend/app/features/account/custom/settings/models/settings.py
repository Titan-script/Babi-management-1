from typing import Optional

from sqlmodel import Field, SQLModel

"""if TYPE_CHECKING:
    from .user import User  
    
"""


class UserSetting(SQLModel, table=True):
    __tablename__ = "user_setting"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True, index=True)

    # Sécurité & Compte
    two_factor_enabled: bool = Field(default=False)
    biometric_login_enabled: bool = Field(default=False)
    profile_visibility: str = Field(default="school_only")  # "public", "school_only", "private"
    account_status: str = Field(default="active")


"""    user: Optional["User"] = Relationship(back_populates="settings")
"""

from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import (
    ApprovalMixin,
    BaseTenant,
    ImageAssetMixin,
    NfcAssetMixin,
    QRCodeAssetMixin,
    UsageTrackerMixin,
)


class UserInfos(
    BaseTenant,
    QRCodeAssetMixin,
    ImageAssetMixin,
    NfcAssetMixin,
    ApprovalMixin,
    UsageTrackerMixin,
    table=True,
):
    __tablename__ = "users"

    full_name: str
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: str = Field(index=True, unique=True)
    birth_date: Optional[str] = None
    firebase_uid: str = Field(unique=True, index=True)

    role: str = Field(default="student")  # 'student', 'teacher', 'educator', 'keeper'
    is_school_admin: bool = Field(default=False)

    # --- Relations ---
    user_preferences: Optional["UserSettings"] = Relationship(back_populates="user")
    user_settings: Optional["SecuritySettings"] = Relationship(back_populates="user")

    invitation_code: Optional["InvitationCode"] = Relationship(back_populates="user")

    storekeeper_profile: Optional["ProfileStoreKeeper"] = Relationship(back_populates="user")
    org: Optional["OrgInfos"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": False}
    )
    # Dans ton modèle User :
    device_sessions: list["UserDeviceSession"] = Relationship(
        back_populates="user", cascade_delete=True
    )

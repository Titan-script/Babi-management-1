from typing import Optional

from pydantic import Field

from app.toolbox import BaseReadSchema, BaseSchema

from ....identity.user.schemas.infos import ProfileInfosNested

# --- USER SETTINGS SCHEMAS ---


class UserSettingBase(BaseSchema):
    two_factor_enabled: Optional[bool] = False
    biometric_login_enabled: Optional[bool] = False
    profile_visibility: Optional[str] = Field(
        default="school_only", description="public, school_only, private"
    )


class UserSettingCreate(UserSettingBase):
    pass


class UserSettingUpdate(BaseSchema):
    two_factor_enabled: Optional[bool] = None
    biometric_login_enabled: Optional[bool] = None
    profile_visibility: Optional[str] = None
    account_status: Optional[str] = None


class UserSettingRead(UserSettingBase, BaseReadSchema):
    user: Optional["ProfileInfosNested"]
    account_status: str


UserSettingRead.model_rebuild()

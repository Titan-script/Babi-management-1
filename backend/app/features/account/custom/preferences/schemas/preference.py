from typing import Optional

from pydantic import Field

from app.toolbox import BaseReadSchema, BaseSchema

from ....identity.user.schemas.infos import ProfileInfosNested


# --- USER PREFERENCES SCHEMAS ---
class UserPreferenceBase(BaseSchema):
    theme: Optional[str] = Field(default="system", description="light, dark ou system")
    language: Optional[str] = Field(default="fr", description="Code langue ex: fr, en")
    push_notifications_enabled: Optional[bool] = True
    email_notifications_enabled: Optional[bool] = True


class UserPreferenceCreate(UserPreferenceBase):
    pass


class UserPreferenceUpdate(BaseSchema):
    theme: Optional[str] = None
    language: Optional[str] = None
    push_notifications_enabled: Optional[bool] = None
    email_notifications_enabled: Optional[bool] = None


class UserPreferenceRead(UserPreferenceBase, BaseReadSchema):
    user: Optional["ProfileInfosNested"]


UserPreferenceRead.model_rebuild()

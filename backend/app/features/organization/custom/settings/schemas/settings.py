from typing import Optional

from app.toolbox import BaseReadSchema, BaseSchema

# OrgSettingsCreate,OrgSettingsRead,OrgSettingsUpdate


class OrgSettingsBase(BaseSchema):
    sms_balance: int
    is_setup_completed: bool


class OrgSettingsUpdate(BaseSchema):
    is_setup_completed: Optional[bool] = None


class OrgSettingsRead(OrgSettingsBase, BaseReadSchema):
    pass


class OrgSettingsNested(OrgSettingsBase, BaseReadSchema):
    pass

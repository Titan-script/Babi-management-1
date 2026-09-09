from datetime import datetime
from typing import Optional

from app.toolbox import BaseReadSchema, BaseSchema

# =================================INVITATIN CODE==========================


class InvitationCodeBase(BaseSchema):
    target_role: str
    purpose: Optional[str] = "RECRUITMENT"
    usage_limit: Optional[int] = 1


class InvitationCodeCreate(InvitationCodeBase):
    pass


class InvitationCodeRead(InvitationCodeBase, BaseReadSchema):
    code: str
    used_count: int
    is_active: bool
    is_expired: bool
    is_approved: bool
    status: str
    expires_at: datetime


class InvitationCodeNested(BaseReadSchema):
    target_role: str

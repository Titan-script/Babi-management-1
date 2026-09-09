from app.common import BaseModel, Optional, datetime


class ExpirySchemaMixin(BaseModel):
    expires_at: Optional[datetime] = None
    is_expired: Optional[bool] = None


class UsageTrackerSchemaMixin(BaseModel):
    usage_limit: Optional[int] = None
    used_count: Optional[int] = None
    is_active: Optional[bool] = None


class ApprovalSchemaMixin(BaseModel):
    is_approved: Optional[bool] = None
    approved_by: Optional[int] = None
    status: Optional[str] = None


class BDESchemaMixin(BaseModel):
    is_bde_member: Optional[bool] = None
    bde_role: Optional[str] = None

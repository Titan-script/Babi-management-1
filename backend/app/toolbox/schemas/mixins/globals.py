from app.common import BaseModel, Optional, datetime

# --- BASE READ SCHEMA AVEC MIXINS ---


class TimeStampedRead(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class SoftDeleteRead(BaseModel):
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None


class IdentifiableRead(BaseModel):
    id: Optional[int] = None

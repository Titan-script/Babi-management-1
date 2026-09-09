from app.common import BaseModel, Optional, datetime


class LifecycleSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    is_active: bool = True


class NotesDescriptionSchemaMixin(BaseModel):
    notes: Optional[str] = None
    description: Optional[str] = None

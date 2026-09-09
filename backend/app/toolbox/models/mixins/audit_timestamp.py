from app.common import Field, Optional, SQLModel, datetime, timezone


class AuditMixin(SQLModel):
    created_by: Optional[int] = Field(default=None, foreign_key="user.id")
    updated_by: Optional[int] = Field(default=None, foreign_key="user.id")


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"server_default": "CURRENT_TIMESTAMP"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={
            "server_default": "CURRENT_TIMESTAMP",
            "onupdate": "CURRENT_TIMESTAMP",
        },
    )


class SoftDeleteMixin(SQLModel):
    is_deleted: bool = Field(default=False)
    deleted_at: Optional[datetime] = Field(default=None)

    def block(self):
        self.is_deleted = True
        self.deleted_at = datetime.now(timezone.utc)

    def unblock(self):
        self.is_deleted = False
        self.deleted_at = None

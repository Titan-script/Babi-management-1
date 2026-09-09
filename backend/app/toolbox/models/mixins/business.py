from app.common import Field, SQLModel, datetime, timezone


class ExpiryMixin(SQLModel):
    expires_at: datetime
    is_expired: bool = Field(default=False)

    def is_valid(self) -> bool:
        if self.is_expired:
            return False
        return datetime.now(timezone.utc) < self.expires_at.replace(tzinfo=timezone.utc)


class UsageTrackerMixin(SQLModel):
    usage_limit: int = Field(default=1)
    used_count: int = Field(default=0)
    is_active: bool = Field(default=False)

    @property
    def is_full(self) -> bool:
        return self.used_count >= self.usage_limit

    def can_be_used(self):
        return self.used_count < self.usage_limit

    def increment(self):
        self.used_count += 1
        if self.used_count >= self.usage_limit and hasattr(self, "mark_as_expired"):
            self.mark_as_expired()


class ApprovalMixin(SQLModel):
    is_approved: bool = Field(default=False)
    approved_by: int | None = None
    status: str = Field(default="pending")


class BDEMixin(SQLModel):
    is_bde_member: bool = Field(default=False)
    bde_role: str | None = None

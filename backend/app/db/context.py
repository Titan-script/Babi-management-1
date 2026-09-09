from app.common import AsyncSession, ContextVar

current_org_id: ContextVar[int] = ContextVar("current_org_id", default=0)
current_user_id: ContextVar[int] = ContextVar("current_user_id", default=0)

db_context: ContextVar[AsyncSession | None] = ContextVar("db_context", default=None)

from app.common import AsyncSession, SQLModel, async_sessionmaker, create_async_engine
from app.core.config import settings

from .context import db_context

# 1. Création de l'engine asynchrone (on utilise postgresql+asyncpg ou sqlite+aiosqlite)
async_engine = create_async_engine(
    settings.DATABASE_URL, echo=False, future=True, pool_size=10, max_overflow=20
)

# 2. Factory de session asynchrone
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


async def create_db_and_tables():
    async with async_engine.begin() as conn:
        # En mode asynchrone, on utilise run_sync pour créer les tables SQLModel
        await conn.run_sync(SQLModel.metadata.create_all)


# 3. La dépendance FastAPI asynchrone pour injecter la session
async def get_db():
    async with AsyncSessionLocal() as session:
        token = db_context.set(session)
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            db_context.reset(token)

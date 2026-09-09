from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .security_settings import SecuritySettingsManager


class SettingsManager(
    SecuritySettingsManager,
):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

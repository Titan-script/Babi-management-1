from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .staff import StaffAuthManager


class StaffManager(
    StaffAuthManager,
):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

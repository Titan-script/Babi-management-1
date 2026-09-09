from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .org import OrgTenantManager


class OrgManager(OrgTenantManager):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

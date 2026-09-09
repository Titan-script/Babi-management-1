from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .invitation import InvitationManager


class InvitationCodeManager(
    InvitationManager,
):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

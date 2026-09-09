""""

from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession


from .login import LoginManager


class AuthManager(
    LoginManager,
):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

""""
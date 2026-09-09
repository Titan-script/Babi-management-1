from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .restaurant import OrderManager


class RestaurantManager(
    OrderManager,
):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

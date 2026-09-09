from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .reception import StockReception
from .sortie import StockOutput
from .stock import RegisterOutput


class InventoryManager(StockReception, StockOutput, RegisterOutput):
    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)

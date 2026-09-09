from fastapi import HTTPException
from sqlmodel import select

from ..models.stock import Stock, StockHistory
from ..schemas.stock import INVStockAdjustmentCreate


class StockOutput:
                
    def __init__(self):
        from app.features.account.identity.user.models.infos import UserInfos
        from app.toolbox.crud.base import BaseCrud

        # Initialisation des sous-CRUD spécifiques si nécessaire
        self.stock_history_crud = BaseCrud(model=StockHistory)
        self.stock_crud = BaseCrud(model=Stock)

    async def adjust_stock(self, data: INVStockAdjustmentCreate):
        """Ajuste manuellement l'inventaire (Async)."""
        stock = self.stock_crud.get_or_404(data.variant_id,self.stock_crud.variant_id)

        old_total = stock.total_quantity
        new_total = data.new_quantity_loose + (data.new_quantity_cartons * stock.quantity_by_carton)
        diff = new_total - old_total

        stock.quantity_loose = data.new_quantity_loose
        stock.quantity_cartons = data.new_quantity_cartons

        self.stock_history_crud.add(
                variant_id=data.variant_id,
                movement_type="ADJUSTMENT",
                quantity=diff,
                comment=f"Correction d'inventaire: {data.comment}",
        )
        self.stock_crud.add(stock)

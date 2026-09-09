import math

from fastapi import HTTPException
from sqlmodel import select

from ..models.stock import Stock, StockHistory
from ..schemas.stock import INVStockOutputCreate


class RegisterOutput:
                    
    def __init__(self):
        from app.features.account.identity.user.models.infos import UserInfos
        from app.toolbox.crud.base import BaseCrud

        # Initialisation des sous-CRUD spécifiques si nécessaire
        self.stock_history_crud = BaseCrud(model=StockHistory)
        self.stock_crud = BaseCrud(model=Stock)

    async def register_output(self, data: INVStockOutputCreate):
        """Enregistre une sortie de stock (Async)."""
        stock = self.stock_crud.get_or_404(data.variant_id,self.stock_crud.variant_id)

        if (hasattr(stock.variant, "is_active") and not stock.variant.is_active):
            raise HTTPException(status_code=404, detail="Produit indisponible ou inactif")

        if stock.total_quantity < data.quantity:
            raise HTTPException(
                status_code=400, detail="Stock insuffisant pour honorer cette sortie"
            )

        if stock.quantity_loose >= data.quantity:
            stock.quantity_loose -= data.quantity
        else:
            needed = data.quantity - stock.quantity_loose
            cartons_to_open = math.ceil(needed / stock.quantity_by_carton)

            stock.quantity_cartons -= cartons_to_open
            stock.quantity_loose = (cartons_to_open * stock.quantity_by_carton) - needed

        self.stock_history_crud.add(
                variant_id=data.variant_id,
                movement_type="OUT",
                quantity=data.quantity,
                comment=data.comment,
            
        )
        self.db.add(stock)
        await self.db.refresh(stock)
        return stock

from fastapi import HTTPException
from sqlmodel import select

from ...catalog.models.catalog import Variant
from ..models.stock import Stock, StockHistory
from ..schemas.stock import INVStockReceptionCreate


class StockReception:
            
    def __init__(self):
        from app.features.account.identity.user.models.infos import UserInfos
        from app.toolbox.crud.base import BaseCrud

        # Initialisation des sous-CRUD spécifiques si nécessaire
        self.variant_crud = BaseCrud(model=Variant)
        self.stock_history_crud = BaseCrud(model=StockHistory)
        self.stock_crud = BaseCrud(model=Stock)

    async def receive_stock(self, data: INVStockReceptionCreate):
        """Réception de stock avec gestion des cartons et vrac (Async & ManuelManager)."""
        variant = self.variant_crud.get_or_404(data.variant_id)
        stock = self.stock_crud.get_or_404(data.variant_id,self.stock_crud.variant_id)

        if not stock:
            stock = Stock(
                variant_id=data.variant_id,
                quantity_cartons=0.0,
                quantity_loose=0.0,
                quantity_by_carton=data.units_per_carton,
            )
            self.db.add(stock)

        stock.quantity_cartons += data.cartons

        units_per_c = stock.quantity_by_carton or data.units_per_carton
        total_received_units = data.cartons * units_per_c

        history = self.stock_history_crud.add(
            variant_id=data.variant_id,
            movement_type="IN",
            quantity=total_received_units,
            comment=f"Réception: {data.comment or 'Aucun commentaire'}",
        )
        return stock

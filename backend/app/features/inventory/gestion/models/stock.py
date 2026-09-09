from typing import Optional

from sqlmodel import Field, Relationship

from app.toolbox import BaseTenant


class Stock(BaseTenant, table=True):
    __tablename__ = "stocks"
    variant_id: int = Field(foreign_key="variants.id", unique=True, index=True)

    quantity_cartons: float = Field(default=0.0)
    quantity_by_carton: float = Field(default=1.0)
    quantity_loose: float = Field(default=0.0)
    total_quantity: float = Field(default=0.0)

    variant: Optional["Variant"] = Relationship(back_populates="stock")

    @property
    def total_quantity(self) -> float:
        return (self.quantity_cartons * self.quantity_by_carton) + self.quantity_loose

    @property
    def is_low(self) -> bool:
        # On utilise la threshold définie dans le variant
        return self.total_quantity <= self.variant.alert_threshold


class StockHistory(BaseTenant, table=True):
    __tablename__ = "stock_histories"
    variant_id: int = Field(foreign_key="variants.id", index=True)
    movement_type: str  # "IN", "OUT", "ADJUSTMENT"
    quantity: float
    comment: Optional[str] = None

    variant: Optional["Variant"] = Relationship(back_populates="stock_history")



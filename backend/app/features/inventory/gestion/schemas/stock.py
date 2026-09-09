from datetime import date
from typing import Optional

from app.toolbox import BaseReadSchema, BaseSchema

from ...catalog.schemas.catalog import INVVariantNested

# --- STOCK OPERATIONS ---


# Schéma pour la réception (IN)
class INVStockReceptionBase(BaseSchema):
    cartons: float
    units_per_carton: float
    comment: Optional[str] = None
    expiry_date: Optional[date] = None


class INVStockReceptionCreate(INVStockReceptionBase):
    variant_id: int


# Schéma pour la sortie (OUT)
class INVStockOutputBase(BaseSchema):
    quantity: float
    comment: Optional[str] = None


class INVStockOutputCreate(INVStockOutputBase):
    variant_id: int


# Schéma pour l'ajustement (Inventaire physique)
class INVStockAdjustmentBase(BaseSchema):
    new_quantity_loose: float
    new_quantity_cartons: float
    comment: str


class INVStockAdjustmentCreate(INVStockAdjustmentBase):
    variant_id: int


# Schémas de lecture INVStock & Historique
class INVStockBase(BaseSchema):
    quantity_loose: float
    total_quantity: float
    quantity_cartons: float
    quantity_cartons: float
    is_low: bool


class INVStockRead(INVStockBase, BaseReadSchema):
    variant: Optional["INVVariantNested"]


class INVStockNested(BaseReadSchema):
    total_quantity: float
    is_low: bool


# Schémas de lecture Historique


class INVStockHistoryBase(BaseSchema):
    movement_type: str
    quantity: float
    comment: Optional[str] = None


class INVStockHistoryRead(INVStockHistoryBase):
    variant: Optional["INVVariantNested"]


class INVStockHistoryNested(BaseReadSchema):
    movement_type: str
    quantity: float

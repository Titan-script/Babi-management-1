from enum import Enum
from typing import List, Optional

from app.toolbox import BaseReadSchema, BaseSchema

from ...catalog.schemas.catalog import INVVariantNested


class PreparationStatus(str, Enum):
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    READY = "READY"
    SERVED = "SERVED"
    CANCELLED = "CANCELLED"


class OrderItemBase(BaseSchema):
    quantity: float
    notes: Optional[str] = None  # Ex: "Sans oignon", "Bien cuit"


class OrderItemCreate(OrderItemBase):
    variant_id: int


class OrderItemRead(OrderItemBase, BaseReadSchema):
    variant: "INVVariantNested"
    unit_price: float


class OrderItemUpdate(OrderItemBase):
    variant_id: int


# Schéma global pour créer la commande
class OrderBase(BaseSchema):
    location_reference: str  # Ex: "TABLE_4" ou "COMPTOIR"
    reduction: Optional[float] = None


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderRead(OrderBase, BaseReadSchema):
    items: List[OrderItemRead]
    payment_method: Optional[str] = None
    total_amount: float


class OrderUpdate(OrderBase):
    items: List[OrderItemUpdate]
    preparation_status: PreparationStatus
    payment_method: Optional[str] = None

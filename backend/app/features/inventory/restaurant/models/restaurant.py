from typing import List, Optional

from sqlmodel import Field, Relationship

from app.toolbox import BaseTenant


class OrderItem(BaseTenant, table=True):
    __tablename__ = "order_items"

    order_id: int = Field(foreign_key="orders.id")
    variant_id: int = Field(foreign_key="variants.id")
    quantity: float
    unit_price: float  # Prix unitaire au moment de la commande

    # Champ pour les instructions spéciales du client
    notes: Optional[str] = None

    order: Optional["Order"] = Relationship(back_populates="items")
    variant: Optional["Variant"] = Relationship()


class Order(BaseTenant, table=True):
    __tablename__ = "orders"

    # Référence de la table ou du client (ex: "TABLE_4", "COMPTOIR")
    location_reference: str = Field(index=True)

    # Statut global de la commande (PENDING, PAID, CANCELLED)
    status: str = Field(default="PENDING")

    # Statut de préparation par la cuisine (PENDING, PREPARING, READY, SERVED)
    preparation_status: str = Field(default="PENDING")

    total_amount: float = Field(default=0.0)
    payment_method: Optional[str] = None  # "CASH", "MOBILE_MONEY", "CARD"
    reduction: Optional[float] = None

    # Relation avec les lignes de la commande (plusieurs articles)
    items: List["OrderItem"] = Relationship(back_populates="order")

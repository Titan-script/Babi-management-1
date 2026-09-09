from typing import List, Optional

from sqlmodel import Field, Relationship

from app.toolbox import BarcodeAssetMixin, BaseTenant


# --- Modèles mis à jour ---
class Category(BaseTenant, table=True):
    __tablename__ = "categories"
    name: str
    description: Optional[str] = None

    products: List["Product"] = Relationship(back_populates="category")


class Product(BaseTenant, table=True):
    __tablename__ = "products"
    category_id: int = Field(foreign_key="categories.id")
    name: str

    category: Optional["Category"] = Relationship(back_populates="category")

    variants: List["Variant"] = Relationship(back_populates="product")


class Variant(BaseTenant, BarcodeAssetMixin, table=True):
    __tablename__ = "variants"
    product_id: int = Field(foreign_key="products.id")
    sku: str = Field(unique=True, index=True)
    name: str
    unit: str = "unit"
    purchase_price: float = 0.0
    selling_price: float = 0.0
    alert_threshold: int = 10
    is_active: bool = True  # Ajouté pour gestion propre

    product: Optional["Product"] = Relationship(back_populates="variants")
    stock: Optional["Stock"] = Relationship(back_populates="variants")
    stock_history: Optional["StockHistory"] = Relationship(back_populates="variant")

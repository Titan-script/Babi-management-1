from typing import List, Optional

from app.toolbox import AssetBarreCodeMixin, BaseReadSchema, BaseSchema


# --- CATEGORY ---
class INVCategoryBase(BaseSchema):
    name: str
    description: Optional[str] = None


class INVCategoryCreate(INVCategoryBase):
    pass


class INVCategoryUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None


class INVCategoryRead(INVCategoryBase, BaseReadSchema):
    products: List["INVProductNested"]


class INVCategoryNested(INVCategoryBase, BaseReadSchema):
    pass


class INVVariantNested(BaseReadSchema):
    sku: str
    name: str


# --- PRODUCT ---
class INVProductBase(BaseSchema):
    name: str


class INVProductCreate(INVProductBase):
    category_id: int


class INVProductUpdate(BaseSchema):
    category_id: Optional[int] = None
    name: Optional[str] = None


class INVProductRead(INVProductBase, BaseReadSchema):
    category: Optional["INVCategoryNested"]
    variants: List["INVVariantNested"]


class INVProductNested(INVProductBase, BaseReadSchema):
    pass


# --- VARIANT (Avec Barcode) ---
class barre_code(AssetBarreCodeMixin):
    pass


class INVVariantBase(BaseSchema):
    sku: str
    name: str
    unit: Optional[str] = "unit"
    purchase_price: Optional[float] = 0.0
    selling_price: Optional[float] = 0.0
    alert_threshold: Optional[int] = 10


class INVVariantCreate(INVVariantBase):
    product_id: int


class INVVariantUpdate(BaseSchema):
    product_id: Optional[int] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    purchase_price: Optional[float] = None
    selling_price: Optional[float] = None
    alert_threshold: Optional[int] = None
    is_delete: Optional[bool] = None


class INVVariantRead(INVVariantBase, barre_code, BaseReadSchema):
    product: Optional["INVProductNested"]

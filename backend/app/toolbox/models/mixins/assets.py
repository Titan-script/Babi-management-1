from app.common import Field, Optional, SQLModel, uuid


class QRCodeAssetMixin(SQLModel):
    sharing_token: str = Field(default_factory=lambda: str(uuid.uuid4()), index=True, unique=True)
    qr_code_url: Optional[str] = Field(default=None, unique=True, index=True)
    qr_code_public_id: Optional[str] = Field(default=None)


class BarcodeAssetMixin(SQLModel):
    barcode_url: Optional[str] = Field(default=None, unique=True, index=True)
    barcode_public_id: Optional[str] = Field(default=None)


class NfcAssetMixin(SQLModel):
    nfc_url: Optional[str] = Field(default=None, unique=True, index=True)
    nfc_public_id: Optional[str] = Field(default=None)  # Correction du "=" manquant


class LogoAssetMixin(SQLModel):
    logo_url: Optional[str] = Field(default=None)
    logo_public_id: Optional[str] = Field(default=None)


class ImageAssetMixin(SQLModel):
    hero_image_url: Optional[str] = Field(default=None)
    hero_image_public_id: Optional[str] = Field(default=None)


class BackgroundAssetMixin(SQLModel):
    login_background_url: Optional[str] = Field(default=None)
    login_background_public_id: Optional[str] = Field(default=None)

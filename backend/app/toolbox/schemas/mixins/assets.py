from app.common import BaseModel, Field, Optional


class AssetLogoMixin(BaseModel):
    logo_url: Optional[str] = Field(default=None)


class AssetBackgroundMixin(BaseModel):
    login_background_url: Optional[str] = Field(default=None)


class AssetImageMixin(BaseModel):
    hero_image_url: Optional[str] = Field(default=None)


class AssetBarreCodeMixin(BaseModel):
    # Code-barres
    barcode_url: Optional[str] = Field(default=None, index=True)


class AssetQrCodeMixin(BaseModel):
    # QR Code
    qr_code_url: Optional[str] = Field(default=None)


class AssetNfcCodeMixin(BaseModel):
    # NFC
    nfc_url: Optional[str] = Field(default=None)

from .crud.base import BaseCrud
from .managers.base import ManuelManager
from .managers.factory_manager import ManagerFactory
from .models.base import BaseOrg, BaseTenant, BaseTenantUID
from .models.mixins.assets import (
    BackgroundAssetMixin,
    BarcodeAssetMixin,
    ImageAssetMixin,
    LogoAssetMixin,
    NfcAssetMixin,
    QRCodeAssetMixin,
)
from .models.mixins.business import ApprovalMixin, BDEMixin, ExpiryMixin, UsageTrackerMixin
from .models.mixins.location import LocationLiveMixin
from .routers.auto.base import AutoRouter
from .routers.manuel.base import ManuelRouter
from .schemas.base import BaseReadSchema, BaseSchema
from .schemas.mixins.adresse import AddressSchemaMixin, GeolocSchemaMixin
from .schemas.mixins.assets import (
    AssetBackgroundMixin,
    AssetBarreCodeMixin,
    AssetImageMixin,
    AssetLogoMixin,
    AssetNfcCodeMixin,
    AssetQrCodeMixin,
)
from .schemas.mixins.auth import (
    AuthMixin,
    BlockedSchemaMixin,
    ContactSchemaMixin,
    EmailMixin,
    PasswordMixin,
)
from .schemas.mixins.bussiness import (
    ApprovalSchemaMixin,
    BDESchemaMixin,
    ExpirySchemaMixin,
    UsageTrackerSchemaMixin,
)
from .schemas.mixins.special import LifecycleSchema, NotesDescriptionSchemaMixin
from .security.base_security import oauth2_scheme, security

__all__ = [
    # schemas
    "BaseOrg",
    "BaseTenant",
    "BaseTenantUID",
    # mixins
    "AuthMixin",
    "EmailMixin",
    "PasswordMixin",
    "LifecycleSchema",
    "NotesDescriptionSchemaMixin",
    "TimestampSchemaMixin",
    "GeolocSchemaMixin",
    "ContactSchemaMixin",
    "AddressSchemaMixin",
    "LocationLiveMixin",
    "QRCodeAssetMixin",
    "BarcodeAssetMixin",
    "NfcAssetMixin",
    "LogoAssetMixin",
    "ImageAssetMixin",
    "BackgroundAssetMixin",
    "ExpiryMixin",
    "UsageTrackerMixin",
    "ApprovalMixin",
    "BDEMixin",
    # schemas
    "BaseSchema",
    "BaseReadSchema",
    # mixins
    "AssetLogoMixin",
    "AssetBackgroundMixin",
    "AssetBarreCodeMixin",
    "AssetQrCodeMixin",
    "AssetNfcCodeMixin",
    "AssetImageMixin",
    # managers
    "ManuelManager",
    "ManagerFactory",
    # routers
    "ManuelRouter",
    "AutoRouter",
    # security
    "oauth2_scheme",
    "security",
    "BaseCrud",
]

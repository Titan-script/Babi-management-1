from typing import Optional

from app.toolbox import (
    ApprovalSchemaMixin,
    AssetImageMixin,
    AssetQrCodeMixin,
    BaseReadSchema,
    BaseSchema,
    BlockedSchemaMixin,
    EmailMixin,
)

# OrgInfos
# OrgInfosCreate,OrgInfosUpdate,OrgInfosRead

# ==================== ORGANIZATION SCHEMAS ====================


class photo(AssetImageMixin):
    pass


class qr_code(AssetQrCodeMixin):
    pass


class OrgInfosBase(EmailMixin, photo, BaseSchema):
    unique_slug: str
    display_name: str
    owner_name: str
    phone: Optional[str] = None


class OrgInfosCreate(OrgInfosBase):
    pass


class OrgInfosUpdate(BaseSchema, BlockedSchemaMixin, ApprovalSchemaMixin):
    unique_slug: Optional[str] = None
    display_name: Optional[str] = None
    owner_name: Optional[str] = None
    phone: Optional[str] = None


class OrgInfosRead(OrgInfosBase, BlockedSchemaMixin, ApprovalSchemaMixin, qr_code, BaseReadSchema):
    portal_token: str


class OrgInfosNested(BaseReadSchema):
    display_name: str
    owner_name: str

from typing import Optional

from pydantic import EmailStr

from app.toolbox import (
    ApprovalSchemaMixin,
    AssetNfcCodeMixin,
    AssetQrCodeMixin,
    AuthMixin,
    BaseReadSchema,
    BaseSchema,
    PasswordMixin,
    UsageTrackerSchemaMixin,
)

# UserInfoCreate,ProfileInfosUpdate,ProfileInfosRead


# =================================USER ==========================
class Qr_Nfc(AssetQrCodeMixin, AssetNfcCodeMixin):
    pass


class Password(PasswordMixin):
    pass


class ProfleInfosBase(AuthMixin):
    full_name: str


class ProfileInfosCreate(
    ProfleInfosBase,
):
    pass


class ProfileInfosRead(
    BaseReadSchema, Password, ProfleInfosBase, Qr_Nfc, ApprovalSchemaMixin, UsageTrackerSchemaMixin
):
    role: Optional[str] = None


class ProfileInfosUpdate(BaseSchema, ApprovalSchemaMixin, UsageTrackerSchemaMixin):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None


class ProfileInfosNested(BaseReadSchema):
    full_name: Optional[str] = None


class UserInfosCreate(BaseSchema):
    infos: "ProfileInfosCreate"
    password: "Password"

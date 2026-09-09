from app.common import BaseModel, EmailStr, Optional


class PasswordMixin(BaseModel):
    firebase_uid: str


class EmailMixin(BaseModel):
    email: EmailStr


class BlockedSchemaMixin(BaseModel):
    is_blocked: Optional[bool] = None


class AuthMixin(EmailMixin, PasswordMixin, BlockedSchemaMixin):
    phone_number: Optional[str] = None


class ContactSchemaMixin(BaseModel):
    phone_number: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None

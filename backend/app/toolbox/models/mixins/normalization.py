from sqlmodel import SQLModel

from app.common import SQLModel, field_validator, re


class NormalizationMixin(SQLModel):
    @field_validator("email", mode="before", check_fields=False)
    @classmethod
    def clean_email(cls, v):
        if v and isinstance(v, str):
            return v.strip().lower()
        return v

    @field_validator("phone", mode="before", check_fields=False)
    @classmethod
    def validate_phone(cls, v):
        if v and isinstance(v, str):
            return re.sub(r"[^\d+]", "", v)
        return v

    @field_validator("matricule", mode="before", check_fields=False)
    @classmethod
    def validate_matricule(cls, v):
        if v and isinstance(v, str):
            return v.strip().upper()
        return v

    @field_validator("nom", "username", mode="before", check_fields=False)
    @classmethod
    def clean_text(cls, v):
        if v and isinstance(v, str):
            return v.strip().capitalize()
        return v

    @field_validator("unique_slug", mode="before", check_fields=False)
    @classmethod
    def slugify_name(cls, v):
        if v and isinstance(v, str):
            return re.sub(r"[^a-z0-9]+", "-", v.lower()).strip("-")
        return v

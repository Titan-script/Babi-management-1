from app.common import SQLModel

from .mixins.audit_timestamp import AuditMixin, SoftDeleteMixin, TimestampMixin
from .mixins.normalization import NormalizationMixin
from .mixins.primary import IntegerPrimaryKeyMixin, TenantMixin, UUIDPrimaryKeyMixin


class BaseGlobal(TimestampMixin, SoftDeleteMixin, NormalizationMixin, SQLModel):
    __abstract__ = True

    model_config = {"arbitrary_types_allowed": True, "from_attributes": True}

    def dict_update(self, data: dict, exclude: list = None):
        """Met à jour dynamiquement les attributs du modèle en excluant les champs sensibles."""
        exclude = exclude or ["id", "created_at"]
        for key, value in data.items():
            if key not in exclude and hasattr(self, key):
                setattr(self, key, value)
        return self


class BaseOrg(BaseGlobal):
    __abstract__ = True


class BaseTenant(BaseOrg, TenantMixin, AuditMixin, IntegerPrimaryKeyMixin):
    __abstract__ = True


class BaseTenantUID(BaseOrg, TenantMixin, AuditMixin, UUIDPrimaryKeyMixin):
    __abstract__ = True

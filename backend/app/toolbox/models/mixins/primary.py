from app.common import Field, Optional, SQLModel, random, string, uuid


class UUIDPrimaryKeyMixin(SQLModel):
    """Mixin pour ajouter une clé primaire UUID v4 universelle."""

    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        index=True,
        nullable=False,
        max_length=36,
    )


class IntegerPrimaryKeyMixin(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)


class TenantMixin(SQLModel):
    """Mixin pour ajouter un champ de locataire (tenant) pour la multi-location."""

    org_id: int = Field(index=True, nullable=False, foreign_key="organisations.id")


class CodeMixin(SQLModel):
    """Mixin pour générer un code alphanumérique unique (ex: SCH-9X2Y)."""

    code: str = Field(
        default_factory=lambda: "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        ),
        index=True,
        unique=True,
        nullable=False,
    )

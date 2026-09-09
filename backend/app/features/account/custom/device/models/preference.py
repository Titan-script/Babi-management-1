from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User  # Remplace par ton modèle User réel si besoin


class UserDeviceSession(SQLModel, table=True):
    __tablename__ = "user_device_session"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)

    # Informations sur l'appareil (pour détecter Android, iOS, PC, etc.)
    device_name: str = Field(default="Unknown Device", description="Nom ou modèle de l'appareil")
    os_type: str = Field(default="unknown", description="Android, iOS, Windows, Mac, Linux")
    ip_address: Optional[str] = Field(default=None, description="Adresse IP de connexion")

    # Token pour identifier et révoquer la session à distance
    refresh_token_hash: str = Field(index=True, unique=True)

    # Suivi temporel et état
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_active_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, description="Permet de couper l'accès à distance")

    # Relation optionnelle vers le User
    user: Optional["User"] = Relationship(back_populates="device_sessions")

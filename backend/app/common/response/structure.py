from app.common import Any, Optional


class Success:
    """Structure de données pour un succès."""

    def __init__(
        self,
        data: Any = None,
        message: str = "Opération réussie",
        notification: Optional[str] = None,
    ):
        self.data = data
        self.message = message
        self.notification = notification


class ErrorBase(Exception):
    """Structure de données pour une erreur métier (lève une exception gérée)."""

    def __init__(
        self,
        message: str,
        code: int = 400,
        error_code: Optional[str] = None,
        notification: Optional[str] = None,
    ):
        self.message = message
        self.code = code
        self.error_code = error_code
        self.notification = notification
        super().__init__(self.message)

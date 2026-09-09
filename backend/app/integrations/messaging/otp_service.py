from app.common import secrets, string, time


class OTPService:
    @staticmethod
    def generate(length: int = 6) -> str:
        digits = string.digits
        code = "".join(secrets.choice(digits) for _ in range(length))
        return code

    @staticmethod
    def is_expired(created_at: float, ttl_seconds: int = 300) -> bool:
        """Vérifie si le code est expiré (défaut 5 minutes)"""
        return (time.time() - created_at) > ttl_seconds

    @staticmethod
    def verify(stored_code: str, provided_code: str) -> bool:
        return secrets.compare_digest(stored_code, provided_code)

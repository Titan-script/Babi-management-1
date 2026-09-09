from app.common import CryptContext, OAuth2PasswordBearer

# tokenUrl pointe vers l'authentification Firebase (ou peut rester symbolique)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class SecurityManager:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # --- Gestion des Mots de Passe ---
    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)


security = SecurityManager()

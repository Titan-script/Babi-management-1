from fastapi import HTTPException, status
from sqlmodel import Session, func, select

from ..models.user import User  # Adapte selon ton modèle User


class UsageLimitService:
    def __init__(self, db: Session, max_allowed_users: int = 3):
        self.db = db
        self.max_allowed_users = max_allowed_users

    def check_can_register_new_user(self) -> None:
        """
        Vérifie si le nombre maximal d'utilisateurs autorisés est atteint.
        Si la limite est atteinte, bloque l'inscription avec une erreur 403.
        """
        # Compte le nombre total d'utilisateurs en base
        statement = select(func.count()).select_from(User)
        total_users = self.db.exec(statement).one()

        if total_users >= self.max_allowed_users:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Limite atteinte : ce système est restreint à un maximum de {self.max_allowed_users} utilisateurs.",
            )


from app.api.deps import get_db  # Ta dépendance habituelle pour la base
from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..schemas.user import UserCreate, UserRead
from ..services.usage_tracker import UsageLimitService

router = APIRouter(prefix="/identity", tags=["Identity & Users"])


@router.post("/register", response_model=UserRead)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. On vérifie la limite avant d'aller plus loin (Max 3 personnes)
    tracker = UsageLimitService(db=db, max_allowed_users=3)
    tracker.check_can_register_new_user()

    # 2. Si c'est bon, on continue la création normale du user...
    # db.add(...)
    # db.commit()

    return {"message": "Utilisateur créé avec succès"}

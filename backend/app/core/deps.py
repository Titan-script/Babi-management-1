from fastapi import Depends, HTTPException, status
from firebase_admin import auth as firebase_auth
from sqlmodel import Session, select

from app.db import current_org_id, current_user_id, db_context
from app.features.account.identity.user.models.infos import UserInfos
from app.toolbox import oauth2_scheme


def get_db():
    """Dépendance locale pour la session DB afin d'éviter les imports circulaires."""
    from app.db.session import get_db as _get_db

    yield from _get_db()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> UserInfos:
    """
    Vérifie le jeton Firebase (Bearer Token), extrait le firebase_uid,
    et récupère l'utilisateur correspondant dans la base de données PostgreSQL.
    """
    try:
        # 1. Vérification du token via le SDK Firebase Admin
        decoded_token = firebase_auth.verify_id_token(token)
        firebase_uid = decoded_token.get("uid")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Jeton d'authentification Firebase invalide ou expiré : {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Recherche de l'utilisateur dans PostgreSQL via son firebase_uid
    statement = select(UserInfos).where(UserInfos.firebase_uid == firebase_uid)
    user = db.exec(statement).first()

    if not user or getattr(user, "is_deleted", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Compte utilisateur introuvable ou bloqué dans la base de données.",
        )

    # 3. Injection optionnelle du user_id dans le contexte global si tu en as besoin
    current_user_id.set(user.id)

    return user


def get_active_org(
    db: Session = Depends(get_db), user: UserInfos = Depends(get_current_user)
) -> int:
    """
    Vérifie l'organisation liée à l'utilisateur et injecte l'ID dans le contexte.
    """
    org = user.organisation

    if not org or getattr(org, "subscription_expired", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Accès refusé : Organisation non trouvée ou abonnement expiré.",
        )

    # Injection dans le contexte global pour le BaseCrud
    current_org_id.set(org.id)
    db_context.set(db)

    return org.id


def get_auth_context(
    user: UserInfos = Depends(get_current_user), org_id: int = Depends(get_active_org)
) -> dict:
    """Dépendance combinée pour injecter tout le contexte sécurisé."""
    return {"user": user, "org_id": org_id, "organisation": user.organisation}

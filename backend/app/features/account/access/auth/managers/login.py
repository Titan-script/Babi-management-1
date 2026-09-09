"""from fastapi import HTTPException
from sqlmodel import select
from features.identity.user.models.infos import UserInfos


class LoginManager:
    async def get_or_sync_user_by_firebase_uid(self, firebase_uid: str):

        Récupère l'utilisateur dans PostgreSQL grâce à son UID Firebase
        lorsqu'il se connecte depuis l'application cliente.

        statement = select(UserInfos).where(UserInfos.firebase_uid == firebase_uid)
        result = await self.db.execute(statement)
        user = result.scalars().first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Compte Firebase authentifié mais profil utilisateur introuvable dans la base de données.",
            )

        # Vérification si le compte est approuvé par l'école
        if hasattr(user, "is_approved") and not user.is_approved:
            raise HTTPException(
                status_code=403,
                detail="Votre compte est en attente d'approbation par l'administration.",
            )

        return {"message": "Connexion et synchronisation réussies.", "user": user}
"""

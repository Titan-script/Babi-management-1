from fastapi import HTTPException
from sqlmodel import select

from ..models.invitation import InvitationCode


class InvitationService:
    async def verify_and_consume_code(self, code_str: str) -> InvitationCode:
        """
        Vérifie la validité d'un code d'invitation et l'incrémente/consomme (Async).
        """
        # 1. Recherche du code en base via select() asynchrone
        statement = select(InvitationCode).where(InvitationCode.code == code_str)
        result = await self.db.execute(statement)
        invitation = result.scalars().first()

        if not invitation:
            raise HTTPException(status_code=404, detail="Code d'invitation introuvable.")

        # 2. Vérification via le mixin ExpiryMixin (is_valid)
        if not invitation.is_valid():
            raise HTTPException(status_code=400, detail="Ce code d'invitation a expiré.")

        # 3. Vérification du statut d'activation et de l'état global
        if not invitation.is_active or invitation.status != "active":
            raise HTTPException(status_code=400, detail="Ce code d'invitation n'est plus actif.")

        # 4. Vérification via le mixin UsageTrackerMixin (can_be_used)
        if not invitation.can_be_used():
            raise HTTPException(
                status_code=400,
                detail="Ce code d'invitation a atteint sa limite d'utilisation.",
            )

        # 5. Incrémentation de l'utilisation
        invitation.increment()

        # 6. Sauvegarde des changements en base (asynchrone)
        self.db.add(invitation)
        await self.db.refresh(invitation)

        return invitation

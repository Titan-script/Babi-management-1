from fastapi import HTTPException
from sqlmodel import select
from app.toolbox import ManuelManager,security

from ..models.security_settings import SecuritySettings

class SecuritySettingsManager():
    async def set_secret_question(self, user_id: int, question: str, answer: str):
        """Enregistre ou met à jour directement la question secrète et sa réponse hachée."""
       answer_hash = security.hash_password(answer)
        
        statement = select(SecuritySettings).where(SecuritySettings.user_id == user_id)
        result = await self.db.execute(statement)
        settings = result.scalars().first()
        
        if not settings:
            settings = SecuritySettings(user_id=user_id)
            self.db.add(settings)
            
        
        settings.secret_question = question
        settings.secret_answer_hash = answer_hash
        
        # Nettoyage des champs "pending" devenus inutiles avec Firebase
        settings.pending_secret_question = None
        settings.pending_secret_answer_hash = None
        
        await self.db.commit()
        await self.db.refresh(settings)
        
        return {"message": "Question secrète configurée avec succès !"}

        async def verify_secret_answer(self, user_id: int, answer: str) -> bool:
            """Vérifie si la réponse fournie à la question secrète est correcte."""
            statement = select(SecuritySettings).where(SecuritySettings.user_id == user_id)
            result = await self.db.execute(statement)
            settings = result.scalars().first()
            
            if not settings or not settings.secret_answer_hash:
                raise HTTPException(status_code=400, detail="Aucune question secrète configurée pour cet utilisateur.")
                
            return security.verify_password(answer, settings.secret_answer_hash)

            
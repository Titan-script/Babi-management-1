from fastapi import HTTPException

from app.features.account.access.code.services.invitation import InvitationService

from .....inventory.gestion.models.assign import ProfileStoreKeeper
from ...user.models.infos import UserInfos
from ..schemas.staff import UserStaffCreate


class StaffAuthManager:
    async def register_staff(self, data: UserStaffCreate):
        """Enregistre un membre du staff en validant le code d'invitation (Async & ManuelManager)."""

        # 1. Vérification et consommation asynchrone du code d'invitation
        invitation = await InvitationService.verify_and_consume_code(data.invitation_code)

        if data.role != invitation.target_role:
            raise HTTPException(
                status_code=400,
                detail=f"Ce code d'invitation est réservé au rôle '{invitation.target_role}'.",
            )

        # 2. Extraction des données de l'utilisateur (sans le mot de passe, géré par Firebase)
        user_raw_data = data.model_dump(
            exclude={
                "confirm_password",
                "invitation_code",
                "store_keeper_data",
            }
        )

        # 3. Création de l'utilisateur de base dans PostgreSQL
        user = UserInfos(**user_raw_data)
        user.email_verified = True
        user.is_approved = True
        self.db.add(user)
        await self.db.flush()

        # 4. Association du profil spécifique au rôle du staff

        if data.role == "store_keeper" and data.store_keeper_data:
            profile = ProfileStoreKeeper(user_id=user.id, **data.store_keeper_data.model_dump())
            self.db.add(profile)

            """if data.role == "teacher" and data.teacher_data:
            profile = ProfileTeacher(user_id=user.id, **data.teacher_data.model_dump())
            self.db.add(profile)
        elif data.role == "educator":
            profile = ProfileEducator(
                user_id=user.id,
                **(data.educator_data.model_dump() if data.educator_data else {}),
            )
            self.db.add(profile)"""

        """elif data.role == "driver" and data.driver_data:
            profile = ProfileDriver(user_id=user.id, **data.driver_data.model_dump())
            self.db.add(profile)
        elif data.role == "dorm_supervisor" and data.dorm_supervisor_data:
            profile = ProfileDormSupervisor(
                user_id=user.id, **data.dorm_supervisor_data.model_dump()
            )
            self.db.add(profile)
        else:
            raise HTTPException(
                status_code=400,
                detail="Données de profil  manquantes ou invalides.",
            )
            """

        await self.db.commit()
        await self.db.refresh(user)

        return {
            "message": f"Compte {data.role} créé et synchronisé avec succès !",
            "user_id": user.id,
        }

from app.features.account.identity.user.models.infos import UserInfos

class UserService:

        def _init_(self):
            from app.toolbox.crud.base import BaseCrud
            # Initialisation des sous-CRUD spécifiques si nécessaire
            self.DeviceSession = BaseCrud(model=DeviceSession)
            self.SettingsUser = BaseCrud(model=SettingsUser)
            self.PreferenceUser = BaseCrud(model=PreferenceUser)
            self.UserInfos = BaseCrud(model=UserInfos)
        
        async def userservice(self):

        user_data = data.model_dump(
                exclude={
                    "confirm_password",
                    "invitation_code",
                    "store_keeper_data",
                }
            )
    user_data.upload({"email_verified" = True,"is_approved" = True,})

    user = self.UserInfos.add(**user_raw_data)

            await self.DeviceSession.add(user_id=user.id)
            await self.SettingsUser.add(user_id=user.id)
            await self.PreferenceUser.add(user_id=user.id)

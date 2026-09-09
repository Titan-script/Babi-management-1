from typing import Optional

from app.features.inventory.gestion.schemas.assign import ProfileStoreKeeperCreate
from app.toolbox import BaseSchema

from ...user.schemas.infos import ProfileInfosCreate


# =================================Staff===========================
class UserStaff(BaseSchema):
    invitation_code: str


class UserStaffCreate(ProfileInfosCreate):
    infos: "ProfileInfosCreate"
    code: "UserStaff"
    store_keeper_data: Optional["ProfileStoreKeeperCreate"] = None


UserStaffCreate.model_rebuild()

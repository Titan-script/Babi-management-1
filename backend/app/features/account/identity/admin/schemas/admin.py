from app.toolbox import BaseReadSchema, BaseSchema

from ...user.schemas.infos import ProfileInfosCreate


# ================================= ProfileAdmin===========================
class AdminInfos(BaseSchema):
    pass


class ProfileAdminCreate(AdminInfos, ProfileInfosCreate):
    pass


class ProfileAdminUpdate(BaseSchema):
    pass


class ProfileAdminRead(BaseReadSchema):
    is_school_admin: bool = True


# ================================= UserAdmin===========================


class UserAdminCreate(ProfileAdminCreate):
    pass

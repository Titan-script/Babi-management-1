from app.toolbox import BaseSchema, PasswordMixin

# ================================LOGIN===========================


class LoginBase(BaseSchema, PasswordMixin):
    login: str


class LoginSchema(LoginBase):
    pass


class LoginResponse(LoginBase):
    pass

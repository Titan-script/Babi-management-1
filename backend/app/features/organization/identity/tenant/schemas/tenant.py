from app.toolbox import BaseSchema

from ....subscription.billing.schemas.billing import OrgBillingCreate
from app.features.account.identity.admin.schemas.admin import UserAdminCreate
from .infos import OrgInfosCreate


class OrgTenantCreate(BaseSchema):
    infos: "OrgInfosCreate"
    admin: "UserAdminCreate"
    subscription: "OrgBillingCreate"


OrgTenantCreate.model_rebuild()

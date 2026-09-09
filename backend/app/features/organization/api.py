from .custom.settings.routers.api import all_routers as custom_settings_routers
from .custom.theme.routers.api import all_routers as custom_theme_routers
from .identity.tenant.routers.api import all_routers as identity_tenant_routers
from .subscription.billing.routers.api import all_routers as subscription_billing_routers
from .subscription.plan.routers.api import all_routers as subscription_plan_routers

all_routers = [
    *custom_settings_routers,
    *custom_theme_routers,
    *identity_tenant_routers,
    *subscription_billing_routers,
    *subscription_plan_routers,
]

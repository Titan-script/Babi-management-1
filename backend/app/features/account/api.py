"""from .access.auth.routers.api import all_routers"""

from .access.code.routers.api import all_routers as acces_code_routers
from .custom.preferences.routers.api import all_routers as custom_preferences_routers
from .custom.settings.routers.api import all_routers as custom_settings_routers
from .identity.admin.routers.api import all_routers as identity_admin_routers
from .identity.staff.routers.api import all_routers as identity_staff_routers
from .identity.user.routers.api import all_routers as identity_user_routers

all_routers = [
    *acces_code_routers,
    *custom_settings_routers,
    *custom_preferences_routers,
    *identity_admin_routers,
    *identity_staff_routers,
    *identity_user_routers,
]

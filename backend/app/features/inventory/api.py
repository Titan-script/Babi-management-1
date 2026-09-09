from .catalog.routers.api import all_routers as catalog_routers
from .gestion.routers.api import all_routers as gestion_routers
from .restaurant.routers.api import all_routers as restaurant_routers

all_routers = [
    *catalog_routers,
    *restaurant_routers,
    *gestion_routers,
]

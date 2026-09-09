from .notifications_ws import notifications_ws_router

# =====================================================================
# 1. LISTE DES ROUTEURS WEBSOCKETS
# =====================================================================

all_routers = [
    *notifications_ws_router,
]

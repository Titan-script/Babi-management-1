from .infos import identity_tenant_routers
from .manuel import manuel_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *identity_tenant_routers,
    *manuel_routers,
]

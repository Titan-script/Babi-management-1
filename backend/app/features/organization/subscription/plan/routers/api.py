from .plan import subscription_plan_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *subscription_plan_routers,
]

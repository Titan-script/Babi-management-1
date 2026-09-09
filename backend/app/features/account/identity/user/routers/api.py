# --- Importation des listes de routeurs de tous les modules ---
from .infos import identity_user_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *identity_user_routers,
]

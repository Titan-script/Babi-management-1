# --- Importation des listes de routeurs de tous les modules ---
from .preference import custom_preference_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *custom_preference_routers,
]

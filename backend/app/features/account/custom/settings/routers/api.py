# --- Importation des listes de routeurs de tous les modules ---
from .settings import custom_settings_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *custom_settings_routers,
]

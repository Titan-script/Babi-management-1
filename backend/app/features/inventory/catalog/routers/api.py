# --- Importation des listes de routeurs de tous les modules ---
from .catalog import catalog_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *catalog_routers,
]

# --- Importation des listes de routeurs de tous les modules ---
from .invitation import invitation_routers
from .manuel import manuel_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *invitation_routers,
    *manuel_routers,
]

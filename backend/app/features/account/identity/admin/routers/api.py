# --- Importation des listes de routeurs de tous les modules ---
from .admin import profil_admin_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *profil_admin_routers,
]

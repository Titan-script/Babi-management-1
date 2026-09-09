# --- Importation des listes de routeurs de tous les modules ---
from .manuel import manuel_routers
from .restaurant import restaurant_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [*manuel_routers, *restaurant_routers]

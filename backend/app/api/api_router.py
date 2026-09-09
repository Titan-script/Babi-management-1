from fastapi import APIRouter, FastAPI

from app.api.websockets.routers.api import all_routers as websocket_routers
from app.common import PREFIX
from app.features.account.api import all_routers as account_routers
from app.features.inventory.api import all_routers as inventory_routers
from app.features.organization.api import all_routers as org_routers

from .root_check import root_check

# ==========================================# 1. AGRÉGATION CENTRALE DE TOUTES LES LISTES DE ROUTEURS===========================
master_routers = [
    *inventory_routers,
    *account_routers,
    *org_routers,
    *websocket_routers,
    root_check,
]

# =============================== FONCTION D'ENREGISTREMENT GLOBAL DANS L'APPLICATION PRINCIPALE======================================
PREFIX = PREFIX.API


def register_routers(app: FastAPI) -> None:
    """
    Parcourt dynamiquement la liste consolidée master_routers et
    enregistre chaque routeur dans l'instance principale de l'application FastAPI.
    """
    for router_item in master_routers:
        # Si c'est déjà un APIRouter instancié, on l'utilise directement.
        # Si c'est une fonction (factory), on l'exécute pour obtenir l'APIRouter.
        if isinstance(router_item, APIRouter):
            actual_router = router_item
        elif callable(router_item):
            actual_router = router_item()
        else:
            continue  # Ignore les éléments invalides s'il y en a

        if actual_router is None:
            continue

        if not isinstance(actual_router, APIRouter):
            continue
        app.include_router(actual_router, prefix=PREFIX)

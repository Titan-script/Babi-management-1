from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from .context import ContextMiddleware


def register_middlewares(app: FastAPI) -> None:
    """
    Enregistre tous les middlewares globaux de l'application FastAPI.
    """
    # Compression des réponses si la taille dépasse 1000 octets
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Middleware personnalisé pour la gestion du contexte multi-tenant (Org-ID)
    app.add_middleware(ContextMiddleware)

    # Configuration des politiques CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

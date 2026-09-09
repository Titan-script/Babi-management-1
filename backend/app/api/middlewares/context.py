from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.db import current_org_id, current_user_id, db_context


class ContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware personnalisé pour gérer les variables de contexte (org_id, user_id, db_context)
    à partir des en-têtes de la requête HTTP et assurer un nettoyage systématique.
    """

    async def dispatch(self, request: Request, call_next):
        # 1. Extraction et configuration de l'org_id (via header X-Org-ID ou équivalent)
        org_id_header = request.headers.get("X-Org-ID")
        org_id = int(org_id_header) if org_id_header and org_id_header.isdigit() else None
        org_token = current_org_id.set(org_id)

        try:
            # 2. On laisse la requête continuer son traitement
            response = await call_next(request)
            return response
        finally:
            # 3. Nettoyage systématique après chaque requête pour éviter les fuites de contexte
            current_user_id.set(None)
            current_org_id.reset(org_token)
            db_context.set(None)

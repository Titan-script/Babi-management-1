# ============================ROUTE RACINE DE VÉRIFICATION =========================================

from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.websocket("/")
def root_check():
    return {"app": "Babi Management API", "status": "online", "version": "1.0.0"}


root_check_router = [router]

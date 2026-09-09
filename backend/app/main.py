import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import register_middlewares, register_routers
from app.core.config import settings

# Initialisation de Sentry via les settings
sentry_sdk.init(dsn=settings.SENTRY_DSN)
"""
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    pass
"""
# Initialisation de l'application FastAPI principale
app = FastAPI(
    title="BABI-MANAGEMENT",
    version="1.0.0",
    description="API officielle de Babi Management",
)
"""    lifespan=lifespan"""

# Enregistrement des middlewares (CORS, GZip, Tenant/School-ID, etc.)
register_middlewares(app)

# Enregistrement global de tous les routeurs de l'application
register_routers(app)


# ======================================GESTIONNAIRE D'EXCEPTIONS GLOBAL==============================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Oups, une erreur technique est survenue.", "detail": str(exc)},
    )


# =============================== LANCEMENT DU SERVEUR ======================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.main.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)

#  uvicorn app.main:app --reload

# http://127.0.0.1:8000/openapi.json

# taskkill /f /im python.exe

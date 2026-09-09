from app.common import Any, JSONResponse, Request


async def Error(request: Request, exc: Any) -> JSONResponse:
    """Intercepte et formate proprement toutes les erreurs de l'API."""
    return JSONResponse(
        status_code=getattr(exc, "code", 400),
        content={
            "error": True,
            "message": getattr(exc, "message", str(exc)),
            "error_code": getattr(exc, "error_code", "INTERNAL_ERROR"),
            "notification": getattr(exc, "notification", None),
        },
    )


__all__ = [
    "Error",
]

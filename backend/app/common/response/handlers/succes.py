from app.common import Any, JSONResponse


def send(response: Any) -> JSONResponse:
    """Formate et retourne une réponse de succès standardisée."""
    data = getattr(response, "data", response)
    message = getattr(response, "message", "Opération réussie")
    notification = getattr(response, "notification", None)

    return JSONResponse(
        status_code=200,
        content={"success": True, "data": data, "message": message, "notification": notification},
    )


__all__ = [
    "send",
]

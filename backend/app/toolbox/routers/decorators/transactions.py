from app.common import HTTPException, logging, wraps
from app.db import db_context


def auto_transaction(func):
    """
    Décorateur unique qui gère :
    1. La transaction (commit/rollback)
    2. La gestion des erreurs (log + HTTPException)
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        session = db_context.get()
        try:
            result = await func(*args, **kwargs)

            # Si c'est une opération d'écriture, on commit
            if session.new or session.dirty or session.deleted:
                session.commit()

            return result

        except Exception as e:
            session.rollback()
            logging.error(f"Erreur dans {func.__name__}: {str(e)}", exc_info=True)

            if isinstance(e, HTTPException):
                raise e

            raise HTTPException(
                status_code=500, detail="Une erreur interne est survenue sur le serveur."
            )

    return wrapper


__all__ = [
    "auto_transaction",
]

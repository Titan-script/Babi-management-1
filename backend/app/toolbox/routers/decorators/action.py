from app.common import logging, send, wraps

logger = logging.getLogger("nova_school")


def action_wrapper(resource: str, action_name: str, notify_func=None):
    """Décorateur pour logger, wrapper et formater les réponses des actions métier."""

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            logger.info(f"[ACTION START] Resource: {resource} | Action: {action_name}")

            try:
                # 1. Exécution de la méthode métier
                result = await func(*args, **kwargs)

                # 2. Trigger notification optionnelle
                if notify_func and hasattr(result, "id"):
                    await notify_func(action_name, result)

                # 3. Log succès et retour formaté
                logger.info(f"[ACTION SUCCESS] {resource} | {action_name}")
                return send(
                    {"data": result, "message": f"Action {action_name} effectuée avec succès."}
                )

            except Exception as e:
                # 4. Log erreur détaillé et propagation
                logger.error(f"[ACTION ERROR] {resource} | {action_name} | Error: {str(e)}")
                raise e

        return wrapper

    return decorator


__all__ = [
    "action_wrapper",
]

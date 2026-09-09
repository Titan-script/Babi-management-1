from app.common import asyncio, functools, time

from .config import logger


def log_action(func):
    """Décorateur pour mesurer le temps d'exécution et logger le succès ou l'erreur d'une fonction."""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        func_name = func.__name__
        start_time = time.perf_counter()

        try:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)

            end_time = time.perf_counter()
            duration = end_time - start_time
            logger.info(f"[SUCCESS] {func_name} | Duration: {duration:.4f}s")
            return result

        except Exception as e:
            end_time = time.perf_counter()
            duration = end_time - start_time
            logger.error(f"[ERROR] {func_name} | Duration: {duration:.4f}s | Message: {str(e)}")
            raise e

    return wrapper

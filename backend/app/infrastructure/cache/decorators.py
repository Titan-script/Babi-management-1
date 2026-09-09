from app.common import Any, Callable, json, wraps

from .config import redis_config as RedisConfig


def cache_response(expire: int = 300) -> Callable:
    """
    Décorateur pour mettre en cache le résultat d'une fonction asynchrone dans Redis.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            # Génération d'une clé de cache unique basée sur le nom de la fonction et ses arguments
            kwargs_str = json.dumps(kwargs, sort_keys=True, default=str)
            cache_key = f"cache:{func.__name__}:{kwargs_str}"

            # 1. Vérification dans le cache Redis
            cached_data = RedisConfig.get(cache_key)
            if cached_data:
                return json.loads(cached_data)

            # 2. Exécution de la fonction d'origine si absent du cache
            result = await func(*args, **kwargs)

            # 3. Stockage du résultat dans Redis avec expiration (TTL en secondes)
            try:
                RedisConfig.setex(cache_key, expire, json.dumps(result, default=str))
            except Exception as e:
                # On évite de bloquer l'application si Redis rencontre un problème d'écriture
                print(f"Erreur d'écriture dans le cache Redis : {e}")

            return result

        return wrapper

    return decorator

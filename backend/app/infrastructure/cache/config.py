from app.common import redis
from app.core import settings

redis_config = redis.from_url(
    url=settings.REDIS_URL, 
    decode_responses=True
)

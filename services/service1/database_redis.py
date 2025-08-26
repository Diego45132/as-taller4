import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(REDIS_URL, decode_responses=True)  # decode=True para obtener strings en lugar de bytes
    return _redis_client

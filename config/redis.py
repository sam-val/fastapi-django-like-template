import redis.asyncio as async_redis

from config.settings import get_settings

settings = get_settings()

redis_client = async_redis.Redis.from_url(
    url=str(settings.REDIS_URI),
    decode_responses=True,  # makes Redis return strings instead of bytes
)


async def get_redis():
    return redis_client


async def shutdown_redis() -> None:
    """
    Closing redis connection
    """
    await redis_client.close()
    await redis_client.connection_pool.disconnect()

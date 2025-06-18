from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import AsyncAdaptedQueuePool, NullPool
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.config.settings import ModeEnum, settings

engine = create_engine(
    url=str(settings.DATABASE_URI),
    echo=settings.DEBUG,
)

async_engine = create_async_engine(
    url=str(settings.ASYNC_DATABASE_URI),
    echo=settings.DEBUG,
    poolclass=(
        NullPool if settings.MODE == ModeEnum.testing else AsyncAdaptedQueuePool
    ),  # Asincio pytest works with NullPool
)

async_session_factory = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

import asyncio
import atexit

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

# Import your all models
from backend.apps.hello.models import *
from backend.config.db import engine  # import from your db module
from backend.config.settings import settings

# Sync session
session = Session(engine)

# Ensure sync session is closed when the script exits
atexit.register(session.close)

async_engine = create_async_engine(
    url=str(settings.ASYNC_DATABASE_URI),
    echo=settings.DEBUG,
    poolclass=NullPool,
)

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Helper to run async code
def arun(coro):
    return asyncio.run(coro)


# Shell banner
banner = """
FastAPI Shell — SQLModel (sync + async)
Available:
- session              : sync SQLModel Session
- async_session_factory: async session factory (use `async with async_session_factory() as s`)
- arun(coro)           : helper to run awaitables in sync shell
- All models from our apps
"""


def main():
    # Start shell
    try:
        from IPython import embed

        embed(
            banner1=banner,
        )
    except ImportError:
        import code

        code.interact(local=locals(), banner=banner)
    finally:
        # close sync session
        session.close()

        # close async session
        try:
            arun(async_engine.dispose())
        except Exception as e:
            print("Warning: Failed to dispose async engine:", e)

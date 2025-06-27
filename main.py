from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from config.redis import shutdown_redis
from config.settings import get_settings
from config.urls import router as root_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Init the app on startup
    """
    # Do stuff when starting

    yield

    # Do stuff when closing

    # redis
    await shutdown_redis()


def create_app() -> FastAPI:
    is_prod = settings.MODE == "prod"

    app = FastAPI(
        title="FastAPI Django-like Template",
        debug=settings.DEBUG,
        version="0.0.2",
        docs_url=None if is_prod else "/docs",
        redoc_url=None if is_prod else "/redoc",
        openapi_url=None if is_prod else "/openapi.json",
        lifespan=lifespan,
    )

    app.include_router(root_router)

    # add pagination
    add_pagination(app)

    return app


app = create_app()

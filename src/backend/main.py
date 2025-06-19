from fastapi import FastAPI
from fastapi_pagination import add_pagination

from backend.config.settings import get_settings
from backend.config.urls import router as root_router

settings = get_settings()


def create_app() -> FastAPI:
    is_prod = settings.MODE == "prod"

    app = FastAPI(
        title="FastAPI Django-like Template",
        debug=settings.DEBUG,
        version="0.0.2",
        docs_url=None if is_prod else "/docs",
        redoc_url=None if is_prod else "/redoc",
        openapi_url=None if is_prod else "/openapi.json",
    )

    app.include_router(root_router)

    # add pagination
    add_pagination(app)

    return app


app = create_app()

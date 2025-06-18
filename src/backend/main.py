from fastapi import FastAPI

from backend.config.settings import get_settings
from backend.config.urls import router as root_router


def create_app() -> FastAPI:
    settings = get_settings()
    is_prod = settings.MODE == "prod"

    app = FastAPI(
        title="FastAPI Django-like Folder Structure",
        debug=settings.DEBUG,
        version="0.0.1",
        docs_url=None if is_prod else "/docs",
        redoc_url=None if is_prod else "/redoc",
        openapi_url=None if is_prod else "/openapi.json",
    )

    app.include_router(root_router)
    return app


app = create_app()

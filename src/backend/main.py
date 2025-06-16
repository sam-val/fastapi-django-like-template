from fastapi import FastAPI

from backend.config.urls import router as root_router

app = FastAPI(
    title="FastAPI Django-like Folder Structure",
    version="0.0.1",
)

app.include_router(root_router)

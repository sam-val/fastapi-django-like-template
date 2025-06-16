from fastapi import APIRouter

from backend.api.urls import api_router

router = APIRouter()
router.include_router(api_router, prefix="/api")

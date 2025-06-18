from fastapi import APIRouter

from .views import router as world_views

router = APIRouter()
router.include_router(world_views, prefix="/v1", tags=["World v1"])

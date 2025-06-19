from fastapi import APIRouter

from .views import router as hello_views

router = APIRouter()
router.include_router(hello_views, prefix="/v1", tags=["Example v1"])

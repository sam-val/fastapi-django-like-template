from fastapi import APIRouter

from apps.example.apis.v2.views import router as example_views

router = APIRouter()
router.include_router(example_views, prefix="/v2", tags=["Example v2"])

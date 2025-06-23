from fastapi import APIRouter

from backend.apps.example_app.apis.v1.views import router as example2_views

router = APIRouter()
router.include_router(example2_views, prefix="/v1", tags=["Example #2, v1"])

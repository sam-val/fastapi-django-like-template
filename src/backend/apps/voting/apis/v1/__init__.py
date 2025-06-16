from fastapi import APIRouter

from .views import router as voting_views

router = APIRouter()
router.include_router(voting_views, prefix="/v1", tags=["Voting v1"])

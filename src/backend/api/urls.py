from fastapi import APIRouter

from backend.apps.example.apis.v1 import router as example_router_v1
from backend.apps.example.apis.v2 import router as example_router_v2
from backend.apps.example_app.apis.v1 import router as example2_router_v1

api_router = APIRouter()

# subapp #1
api_router.include_router(example_router_v1, prefix="/example")
api_router.include_router(example_router_v2, prefix="/example")

# subapp #2
api_router.include_router(example2_router_v1, prefix="/example2")

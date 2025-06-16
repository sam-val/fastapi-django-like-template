from fastapi import APIRouter

from backend.apps.hello.apis.v1 import router as hello_router_v1
from backend.apps.hello.apis.v2 import router as hello_router_v2
from backend.apps.voting.apis.v1 import router as voting_router_v1

api_router = APIRouter()

# hello subapp
api_router.include_router(hello_router_v1, prefix="/hello")
api_router.include_router(hello_router_v2, prefix="/hello")

# voting subapp
api_router.include_router(voting_router_v1, prefix="/voting")

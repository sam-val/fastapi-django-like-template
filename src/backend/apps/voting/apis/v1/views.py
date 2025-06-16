from fastapi import APIRouter
from fastapi.responses import JSONResponse

from backend.config.settings import settings

router = APIRouter()


@router.get("/votes")
def votes():
    print("dump: ", settings.model_dump())
    return JSONResponse(content={"message": "Hello, world!"})

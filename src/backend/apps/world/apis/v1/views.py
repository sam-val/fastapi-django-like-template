from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/world")
def world():
    return JSONResponse(content={"message": "World, hello!"})

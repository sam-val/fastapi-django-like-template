from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/example2")
def example2():
    return JSONResponse(content={"message": "World, hello!"})

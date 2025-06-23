from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/example")
def hello_world():
    return JSONResponse(content={"message": "Hello, world 2!"})

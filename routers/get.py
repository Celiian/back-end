from fastapi import APIRouter

router = APIRouter()


@router.get("/get")
async def hello():
    return {"message": "Get page"}
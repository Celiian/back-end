from fastapi import APIRouter

router = APIRouter()


@router.get("/put")
async def hello():
    return {"message": "Put page"}
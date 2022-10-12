from fastapi import APIRouter

router = APIRouter()


@router.get("/patch")
async def hello():
    return {"message": "Patch page"}
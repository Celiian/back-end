from fastapi import APIRouter

router = APIRouter()


@router.get("/delete")
async def hello():
    return {"message": "Delete page"}
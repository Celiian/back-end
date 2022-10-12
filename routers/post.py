from fastapi import APIRouter

router = APIRouter()


@router.get("/post")
async def hello():
    return {"message": "Post page"}
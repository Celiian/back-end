from fastapi import APIRouter
from db.post import postEnclosure
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/enclosures")
def post_enclosure(biome: str, maintenance_cost: str):
    data = (biome, maintenance_cost)
    res = postEnclosure(data)
    if res:
        return JSONResponse(
            status_code=200,
            content="Successful"
        )
    else:
        return JSONResponse(
            status_code=400,
            content="Failed"
        )


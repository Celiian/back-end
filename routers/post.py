from fastapi import APIRouter
from db.post import postEnclosure
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/enclosures")
def post_enclosure(biome: str, maintenance_cost: str):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param biome: The biome string of the enclosure, in the existing biomes
    :param maintenance_cost: The daily cost of maintenance of the enclosure, as a string
    :return: JSON The response with a status code and a message
    """
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


from fastapi import APIRouter
from db.post import postEnclosure
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class ItemEnclosure(BaseModel):
    biome: str
    maintenance_cost: str


@router.post("/enclosures")
def post_enclosure(body: ItemEnclosure):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param biome: STRING REQUIRED The biome string of the enclosure, in the existing biomes
    :param maintenance_cost: STRING REQUIRED The daily cost of maintenance of the enclosure, as a string
    :return: JSON The response with a status code and a message
    """
    print(body.biome, body.maintenance_cost)
    data = (body.biome, body.maintenance_cost)
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


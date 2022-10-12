from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.patch import patch_enclosures

router = APIRouter()


class Item(BaseModel):
    cost: str | None
    biome: str | None


@router.patch("/enclosures/{id}")
async def enclosure(id: int, body: Item):
    """
    Modify an enclosure

    :param id: INT REQUIRED id of an enclosure
    :param body: LIST parameters and values for patch_enclosures
    :return: Message Table updated or not
    """
    cost = body.cost
    biome = body.biome
    print(body)

    res = patch_enclosures(id, cost, biome)

    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "Table updated"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "Table not updated"}
        )
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.patch import patch_enclosures, patch_breeds

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


class Breed(BaseModel):
    food_eaten_daily: int | None
    regime_type: str | None
    era: str | None
    biome_needed: str | None
    price: int | None


@router.patch("/breeds/{name}")
def breed(name: str, body: Breed):
    """
    Edit breed

    :param name: STRING REQUIRED breed name
    :param body: LIST parameters and values for patch_breeds
    :return: Message Table updated or not
    """
    food_eaten_daily = body.food_eaten_daily
    regime_type = body.regime_type
    era = body.era
    biome_needed = body.biome_needed
    price = body.price

    print(body)

    res = patch_breeds(name, food_eaten_daily, regime_type, era, biome_needed, price)

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


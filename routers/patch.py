from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.patch import patch_enclosures, patch_employees

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


class Employee(BaseModel):
    id_team: int | None
    family_name: str | None
    phone_number: int | None
    emergency_contact: str | None


@router.patch("/employees/{id}")
def employees(id: int, body: Employee):
    """
    Edit employees informations

    :param id: INT REQUIRED id of an employee
    :param body: LIST parameters and values for patch_employees
    :return: Message Table updated or not
    """
    id_team = body.id_team
    family_name = body.family_name
    phone_number = body.phone_number
    emergency_contact = body.emergency_contact

    print(body)

    res = patch_employees(id, id_team, family_name, phone_number, emergency_contact)

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

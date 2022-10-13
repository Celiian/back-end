from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.patch import *

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




class Dino(BaseModel):
    id_enclosure: int | None
    gender: str | None
    height: int | None
    weight: int | None
    id_employees: int | None


@router.patch("/dinosaurs/{name}")
def dinosaurs(name: str, body: Dino):
    """
    Edit a dinosaur informations

    :param name: STRING REQUIRED dinosaur name
    :param body: LIST parameters and values for patch_dinosaurs
    :return: Message Table updated or not
    """
    id_enclosure = body.id_enclosure
    gender = body.gender
    height = body.height
    weight = body.weight
    id_employees = body.id_employees

    print(name)
    print(body)

    res = patch_dinosaurs(name, id_enclosure, gender, height, weight, id_employees)

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

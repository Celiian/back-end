from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.patch import *

router = APIRouter()


class Response(BaseModel):
    status_code: int
    content: str


class Item(BaseModel):
    cost: str | None
    biome: str | None


@router.patch("/enclosures/{id_enclosure}",
              status_code=200,
              description="Edit an enclosure",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
async def enclosure(id_enclosure: int, body: Item):
    """
    Modify an enclosure

    :param id_enclosure: INT REQUIRED id of an enclosure
    :param body: CLASS of parameters and values for patch_enclosures
    :return: Message Table updated or not
    """
    cost = body.cost
    biome = body.biome

    res = patch_enclosures(id_enclosure, cost, biome)

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


@router.patch("/breeds/{name}",
              status_code=200,
              description="Edit an breed",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def breed(name: str, body: Breed):
    """
    Edit breed

    :param name: STRING REQUIRED breed name
    :param body: CLASS of parameters and values for patch_breeds
    :return: Message Table updated or not
    """
    food_eaten_daily = body.food_eaten_daily
    regime_type = body.regime_type
    era = body.era
    biome_needed = body.biome_needed
    price = body.price

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


@router.patch("/dinosaurs/{name}",
              status_code=200,
              description="Edit an dinosaur",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def dinosaurs(name: str, body: Dino):
    """
    Edit dinosaur information

    :param name: STRING REQUIRED dinosaur name
    :param body: CLASS of parameters and values for patch_dinosaurs
    :return: Message Table updated or not
    """
    id_enclosure = body.id_enclosure
    gender = body.gender
    height = body.height
    weight = body.weight
    id_employees = body.id_employees

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


@router.patch("/employees/{id_employees}",
              status_code=200,
              description="Edit an employee",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def employees(id_employees: int, body: Employee):
    """
    Edit employees information

    :param id_employees: INT REQUIRED id of an employee
    :param body: CLASS of parameters and values for patch_employees
    :return: Message Table updated or not
    """
    id_team = body.id_team
    family_name = body.family_name
    phone_number = body.phone_number
    emergency_contact = body.emergency_contact

    res = patch_employees(id_employees, id_team, family_name, phone_number, emergency_contact)

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


class Teams(BaseModel):
    team_type: str | None
    vehicle_type: str | None


@router.patch("/teams/{id_teams}",
              status_code=200,
              description="Edit a team",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def team(id_teams: int, body: Teams):
    """
    Edit some team information

    :param id_teams: INT REQUIRED id of a team
    :param body: CLASS of parameters and values for patch_teams
    :return: Message Table updated or not
    """
    team_type = body.team_type
    vehicle_type = body.vehicle_type

    res = patch_teams(id_teams, team_type, vehicle_type)

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


class TeamsOrga(BaseModel):
    id_enclosure: int
    id_team: int
    new_id_enclosure: int | None
    new_id_team: int | None


@router.patch("/teams_organisation",
              status_code=200,
              description="Edit a team organisation (link between teams and enclosures)",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def teams_organisation(body: TeamsOrga):
    """
    Edit the link between team and enclosure

    :param body: CLASS of parameters and values for patch_teams_orga
    :return:Message Table updated or not
    """

    id_team = body.id_team
    id_enclosure = body.id_enclosure
    new_id_enclosure = body.new_id_enclosure
    new_id_team = body.new_id_team

    res = patch_teams_orga(id_enclosure, id_team, new_id_enclosure, new_id_team)

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


class FoodSupplies(BaseModel):
    price: int | None


@router.patch("/food_supplies/{food_type}",
              status_code=200,
              description="Edit a food supplies price",
              responses={
                  400: {"model": Response},
                  409: {"model": Response}
              },
              response_model=Response
              )
def food_supplies(food_type: str, body: FoodSupplies):
    """
    Edit food type price

    :param food_type: INT REQUIRED food type
    :param body: CLASS of parameters and values for patch_food_supplies
    :return: Message Table updated or not
    """
    price = body.price

    print(body)

    res = patch_food_supplies(food_type, price)

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

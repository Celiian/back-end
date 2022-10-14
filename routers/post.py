import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.post import *

router = APIRouter()


class Response(BaseModel):
    status_code: int
    content: str


class ItemTeamOrganisation(BaseModel):
    """
    Formats input values before they are used in the query
    """
    id_enclosure: int
    id_team: int


@router.post("/team_organisation",
             status_code=201,
             description="Add a team organisation",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def team_organisation(body: ItemTeamOrganisation):
    """
    Calls postTeamOrganisation function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.id_enclosure, body.id_team)
    res = post_team_organisation(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemTeam(BaseModel):
    """
    Formats input values before they are used in the query
    """
    team_type: str
    vehicle_type: str


@router.post("/teams",
             status_code=201,
             description="Add a team",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def team(body: ItemTeam):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.team_type, body.vehicle_type)
    res = post_team(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemFood(BaseModel):
    """
    Formats input values before they are used in the query
    """
    food_type: str
    price: int


@router.post("/food_supplies",
             status_code=201,
             description="Add a food type",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def food(body: ItemFood):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.food_type, body.price)
    res = post_food(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemBreed(BaseModel):
    """
    Formats input values before they are used in the query
    """
    breed_name: str
    food_eaten_daily: int
    regime_type: str
    era: str
    biome_needed: str
    price: int


@router.post("/breed",
             status_code=201,
             description="Add a breed of dinosaurs",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def breed(body: ItemBreed):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.breed_name, body.food_eaten_daily, body.regime_type, body.era, body.biome_needed, body.price)
    res = post_breed(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemDinosaur(BaseModel):
    """
    Formats input values before they are used in the query
    """
    dinosaur_name: str
    breed_name: str
    id_enclosure: int
    creation_date: datetime.date
    gender: str
    height: int
    weight: int
    id_employees: int


@router.post("/dinosaurs",
             status_code=201,
             description="Add a dinosaur",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def dinosaur(body: ItemDinosaur):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (
        body.dinosaur_name, body.breed_name, body.id_enclosure, body.creation_date, body.gender, body.height,
        body.weight,
        body.id_employees)
    res = post_dinosaur(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemEnclosure(BaseModel):
    """
    Formats input values before they are used in the query
    """
    biome: str
    maintenance_cost: str


@router.post("/enclosures",
             status_code=201,
             description="Add an enclosure",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def enclosure(body: ItemEnclosure):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: params inside body
        biome: STRING REQUIRED The biome string of the enclosure, in the existing biomes
        maintenance_cost: STRING REQUIRED The daily cost of maintenance of the enclosure, as a string
    :return: JSON The response with a status code and a message
    """
    data = (body.biome, body.maintenance_cost)
    res = post_enclosure(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )


class ItemEmployee(BaseModel):
    """
    Formats input values before they are used in the query
    """
    id_team: int
    family_name: str
    surname: str
    phone_number: str
    social_security_number: str
    emergency_contact: str


@router.post("/employees",
             status_code=201,
             description="Add an employee",
             responses={
                 400: {"model": Response},
                 409: {"model": Response}
             })
def employee(body: ItemEmployee):
    """
    Calls postEmployee function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: params inside the body :
        id_team: INT REQUIRED of the team the employee is attributed to
        family_name: STRING  guess..
        surname: STRING REQUIRED guess...
        phone_number: STRING REQUIRED guess.
        social_security_number: STRING REQUIRED guess....
        emergency_contact: STRING REQUIRED guess...
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.id_team, body.family_name, body.surname, body.phone_number, body.social_security_number,
            body.emergency_contact)
    res = post_employee(data)

    return JSONResponse(
        status_code=201,
        content=res["message"]
    )

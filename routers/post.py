import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.post import postTeam
from db.post import postFood
from db.post import postBreed
from db.post import postDinosaur
from db.post import postEnclosure
from db.post import postEmployee


router = APIRouter()


class ItemTeam(BaseModel):
    """
    Formats input values before they are used in the query
    """
    team_type: str
    vehicle_type: str


@router.post("/teams")
def post_team(body: ItemTeam):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.team_type, body.vehicle_type)
    res = postTeam(data)
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


class ItemFood(BaseModel):
    """
    Formats input values before they are used in the query
    """
    food_type: str
    price: int


@router.post("/food_supplies")
def post_food(body: ItemFood):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.food_type, body.price)
    res = postFood(data)
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


@router.post("/breed")
def post_breed(body: ItemBreed):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.breed_name, body.food_eaten_daily, body.regime_type, body.era, body.biome_needed, body.price)
    res = postBreed(data)
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
    weigh: int
    id_employees: int


@router.post("/dinosaurs")
def post_dinosaur(body: ItemDinosaur):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param body: CLASS OBJECT REQUIRED Contains all parameters of the post query
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.dinosaur_name, body.breed_name, body.id_enclosure, body.creation_date, body.gender, body.height, body.weigh, body.id_employees)
    res = postDinosaur(data)
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


class ItemEnclosure(BaseModel):
    """
    Formats input values before they are used in the query
    """
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


class ItemEmployee(BaseModel):
    """
    Formats input values before they are used in the query
    """
    id_team: int
    family_name: str
    surname: str
    phone_number: str
    social_security_member: str
    emergency_contact: str

@router.post("/employees")
def post_employee(body: ItemEmployee):
    """
    Calls postEmployee function using url parameters as parameter, then returns whether post fails or succeeds

    :param id_team: INT REQUIRED of the team the employee is attributed to
    :param family_name: STRING  guess..
    :param surname: STRING REQUIRED guess...
    :param phone_number: STRING REQUIRED guess.
    :param social_security_member: STRING REQUIRED guess....
    :param emergency_contact: STRING REQUIRED guess...
    :return: JSON REQUIRED The response with a status code and a message
    """
    data = (body.id_team, body.family_name, body.surname, body.phone_number, body.social_security_member, body.emergency_contact)
    res = postEmployee(data)
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
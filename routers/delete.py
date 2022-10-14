from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.delete import *

router = APIRouter()


class Item(BaseModel):
    id: int


class Response(BaseModel):
    status_code: int
    content: str


@router.delete("/enclosures/{enclosure_id}",
               status_code=200,
               description="Delete an enclosure",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def enclosures(enclosure_id: int):
    """
    Send all enclosures

    :param enclosure_id: INT REQUIRED Id of the enclosure
    :return: JSON A status code and a message
    """
    res = delete_enclosure(enclosure_id)

    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


@router.delete("/teams/{team_id}",
               status_code=200,
               description="Delete a team",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def teams(team_id: int):
    """
    Send all enclosures

    :param team_id: INT REQUIRED Id of the team
    :return: JSON A status code and a message
    """
    res = delete_team(team_id)

    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


@router.delete("/food_supplies/{food_name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def food_supply(food_name: str):
    """
    Delete a food supply

    :param food_name: STR REQUIRED Name of the food supply
    :return: JSON A status code and a message
    """
    res = delete_food_supply(food_name)

    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


@router.delete("/employees/{employee_id}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def employees(employee_id: int):
    """
    Delete a food supply

    :param employee_id: INT REQUIRED Id of the employee
    :return: JSON A status code and a message
    """
    res = delete_employees(employee_id)

    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


@router.delete("/dinosaurs/{dinosaur_name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def dinosaurs(dinosaur_name: str):
    """
    Delete a dinosaur

    :param dinosaur_name: STR REQUIRED Name of the dinosaur
    :return: JSON A status code and a message
    """
    res = delete_dinosaurs(dinosaur_name)
    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


@router.delete("/breeds/{breed_name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def breeds(breed_name: str):
    """
    Delete a breeds

    :param breed_name: STR REQUIRED Name of the breed
    :return: JSON A status code and a message
    """
    res = delete_breeds(breed_name)
    return JSONResponse(
        status_code=200,
        content=res["message"]
    )


class teams_organisation_ids(BaseModel):
    id_team: int
    id_enclosure: int


@router.delete("/teams_organisation/",
               status_code=200,
               description="Delete a link between a team and an enclosure",
               responses={
                   400: {"model": Response},
                   409: {"model": Response}
               },
               response_model=Response
               )
async def teams_organisation(body: teams_organisation_ids):
    """
    Delete a link between a team and an enclosure
    :param body: OBJECT (class) REQUIRED Contain Id of the enclosure and Id of the team
    :return: JSON A status code and a message
    """
    res = delete_teams_organisation(body.id_team, body.id_enclosure)
    return JSONResponse(
        status_code=200,
        content=res["message"]
    )

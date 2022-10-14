from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.delete import *

router = APIRouter()


class Item(BaseModel):
    id: int


class Message(BaseModel):
    message: str


@router.delete("/enclosures/{id}",
               status_code=200,
               description="Delete an enclosure",
               responses={
                   400: {"model": Message}
               })
async def enclosures(id: int):
    """
    Send all enclosures

    :return: JSON A status code and the data
    """
    res = delete_enclosure(id)

    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


@router.delete("/teams/{id}",
               status_code=200,
               description="Delete a team",
               responses={
                   400: {"model": Message}
               })
async def teams(id: int):
    """
    Send all enclosures

    :return: JSON A status code and the data
    """
    res = delete_team(id)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


@router.delete("/food_supplies/{food_name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Message}
               }
               )
async def food_supply(food_name: str):
    """
    Delete a food supply

    :return: JSON A status code and the data
    """
    res = delete_food_supply(food_name)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


@router.delete("/employees/{id}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Message}
               }
               )
async def employees(id: int):
    """
    Delete a food supply

    :return: JSON A status code and the data
    """
    res = delete_employees(id)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


@router.delete("/dinosaurs/{name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Message}
               }
               )
async def dinosaurs(name: str):
    """
    Delete a dinosaur

    :return: JSON A status code and the data
    """
    res = delete_dinosaurs(name)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


@router.delete("/breeds/{name}",
               status_code=200,
               description="Delete a food supply",
               responses={
                   400: {"model": Message}
               }
               )
async def breeds(name: str):
    """
    Delete a breeds

    :return: JSON A status code and the data
    """
    res = delete_breeds(name)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


class item(BaseModel):
    id_team: int
    id_enclosure: int


@router.delete("/teams_organisation/",
               status_code=200,
               description="Delete a link between a team and an enclosure",
               responses={
                   400: {"model": Message}
               }
               )
async def teams_organisation(body: item):
    """
    Delete a link between a team and an enclosure

    :return: JSON A status code and the data
    """
    res = delete_teams_organisation(body.id_team, body.id_enclosure)
    return JSONResponse(
        status_code=200,
        content={"Message": res["message"]}
    )


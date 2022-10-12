from fastapi import APIRouter
from db.get import *
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class Message(BaseModel):
    message: str


@router.get("/enclosures", status_code=200,
            description="Get all existing enclosures", )
async def enclosures():
    """
    Send all enclosures

    :return: JSON A status code and the data
    """
    data = get_enclosures()
    return JSONResponse(
        status_code=200,
        content=data
    )


@router.get("/enclosures/{id}",
            status_code=200,
            description="Get the information of a specific enclosure",
            responses={
                404: {"model": Message}
            })
async def enclosure(id: int):
    """
    Send a specific enclosure

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_enclosure(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/enclosures/{id}/dinosaurs",
            status_code=200,
            description="Get all the dinosaurs living in a specific enclosure",
            responses={
                404: {"model": Message}
            })
async def enclosure_dinosaurs(id: int):
    """
    Send all dinosaurs living in an enclosure

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_enclosure_dinosaurs(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/enclosures/{id}/teams",
            status_code=200,
            description="Get all the teams working on a specific enclosure",
            responses={
                404: {"model": Message}
            })
async def enclosure_teams(id: int):
    """
    Send all teams working in an enclosure

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_enclosure_teams(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/enclosures/{id}/teams/employees",
            status_code=200,
            description="Get all the employees working on a specific enclosure",
            responses={
                404: {"model": Message}
            })
async def enclosure_teams_employees(id: int):
    """
    Send all employees working in an enclosure

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_enclosure_teams_employees(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/teams",
            status_code=200,
            description="Get all the teams",
            responses={
                404: {"model": Message}
            })
async def teams():
    """
    Send all teams

    :return:JSON A status code and the data
    """
    data = get_teams()
    return JSONResponse(
        status_code=200,
        content=data
    )


@router.get("/teams/{id}",
            status_code=200,
            description="Get a specific team",
            responses={
                404: {"model": Message}
            })
async def team(id: int):
    """
    Send a specific team

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_team(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/teams/{id}/employees",
            status_code=200,
            description="Get all employees of a team",
            responses={
                404: {"model": Message}
            })
async def team_employees(id: int):
    """
    Send all employees of a team

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_team_employees(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/teams/{id}/enclosures",
            status_code=200,
            description="Get all enclosures managed by a team",
            responses={
                404: {"model": Message}
            })
async def team_enclosures(id: int):
    """
<<<<<<< HEAD
    Send all enclosures managed by a team
=======
    Send a all enclosures managed by a team
>>>>>>> 4c4cf02 (FEATURE/ teams request done, commented and clean)

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_team_enclosures(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/employees",
            status_code=200,
            description="Get all emploeyees",
            responses={
                404: {"model": Message}
            })
async def employees():
    """
    Send all employees

    :return: JSON A status code and the data
    """
    data = get_employees()
    return JSONResponse(
        status_code=200,
        content=data
    )


@router.get("/employees/{id}",
            status_code=200,
            description="Get an employee",
            responses={
                404: {"model": Message}
            })
async def employee(id: int):
    """
    Send one specified employee

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_employee(id)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/food_supplies",
            status_code=200,
            description="Get all food supplies",
            responses={
                404: {"model": Message}
            })
async def food_supplies():
    """
    Send all food supplies

    :return: JSON A status code and the data
    """
    data = get_food_supplies()
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )


@router.get("/food_supplies/{food_type}",
            status_code=200,
            description="Get one food supply",
            responses={
                404: {"model": Message}
            })
async def food_supply(food_type: str):
    """
    Send one specified employee

    :param id: INT REQUIRED The id of the enclosure
    :return: JSON A status code and the data
    """
    data = get_food_supply(food_type)
    if data:
        return JSONResponse(
            status_code=200,
            content=data
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist"}
        )
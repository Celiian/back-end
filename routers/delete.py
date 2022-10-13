from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.delete import *

router = APIRouter()


class Item(BaseModel):
    id: int


@router.delete("/enclosures/{id}",
               status_code=200,
               description="Delete an enclosure"
               )
async def enclosures(id: int):
    """
    Send all enclosures

    :return: JSON A status code and the data
    """
    res = delete_enclosure(id)
    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist",
                     "Error": res
                     }
        )


@router.delete("/teams/{id}",
               status_code=200,
               description="Delete a team"
               )
async def teams(id: int):
    """
    Send all enclosures

    :return: JSON A status code and the data
    """
    res = delete_team(id)
    if res == "True":
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist",
                     "Error": res
                     }
        )


@router.delete("/food_supplies/{food_name}",
               status_code=200,
               description="Delete a food supply"
               )
async def food_supply(food_name: str):
    """
    Delete a food supply

    :return: JSON A status code and the data
    """
    res = delete_food_supply(food_name)
    if res == "True":
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this name does not exist",
                     "Error": res
                     }
        )


@router.delete("/employees/{id}",
               status_code=200,
               description="Delete a food supply"
               )
async def employees(id: int):
    """
    Delete a food supply

    :return: JSON A status code and the data
    """
    res = delete_employees(id)
    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this id does not exist",
                     "Error": res
                     }
        )


@router.delete("/dinosaurs/{name}",
               status_code=200,
               description="Delete a food supply"
               )
async def dinosaurs(name: str):
    """
    Delete a dinosaur

    :return: JSON A status code and the data
    """
    res = delete_dinosaurs(name)
    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this name does not exist",
                     "Error": res
                     }
        )


@router.delete("/breeds/{name}",
               status_code=200,
               description="Delete a food supply"
               )
async def breeds(name: str):
    """
    Delete a breeds

    :return: JSON A status code and the data
    """
    res = delete_breeds(name)
    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "this name does not exist",
                     "Error": res
                     }
        )


class item(BaseModel):
    id_team: int
    id_enclosure: int


@router.delete("/teams_organisation/",
               status_code=200,
               description="Delete a link between a team and an enclosure"
               )
async def teams_organisation(body: item):
    """
    Delete a link between a team and an enclosure

    :return: JSON A status code and the data
    """
    res = delete_teams_organisation(body.id_team, body.id_enclosure)
    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "deleted successfully"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "one of the id does not exist",
                     "Error": res
                     }
        )

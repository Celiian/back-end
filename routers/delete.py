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
    res = delete_enclosures(id)
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

import datetime

from fastapi import APIRouter
from db.post import postDinosaur
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class ItemDinosaur(BaseModel):
    """
    Formats input values because they are used in the query
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

    :param body: CLASS OBJECT Contains all parameters of the post query
    :return: JSON The response with a status code and a message
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
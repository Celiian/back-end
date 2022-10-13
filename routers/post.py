from fastapi import APIRouter
from db.post import postEmployee
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

class ItemEmployee(BaseModel):
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
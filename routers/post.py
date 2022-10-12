from fastapi import APIRouter
from db.post import postEnclosure
from db.post import postEmployee
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/enclosures")
def post_enclosure(biome: str, maintenance_cost: str):
    """
    Calls postEnclosure function using url parameters as parameter, then returns whether post fails or succeeds

    :param biome: The biome string of the enclosure, in the existing biomes
    :param maintenance_cost: The daily cost of maintenance of the enclosure, as a string
    :return: JSON The response with a status code and a message
    """
    data = (biome, maintenance_cost)
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


@router.post("/employees")
def post_employee(id_team: int, family_name: str, surname: str, phone_number: str, social_security_member: str, emergency_contact: str):
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
    data = (id_team, family_name, surname, phone_number, social_security_member, emergency_contact)
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
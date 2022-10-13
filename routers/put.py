from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.put import put_employees

router = APIRouter()


class ItemEmployee(BaseModel):
    """
    *insert desc here
    """
    id_team: int | None
    family_name: str | None
    surname: str | None
    phone_number: str | None
    social_security_number: str | None
    emergency_contact: str | None


@router.put("/employees/{id_employee_member}")
async def employees(id_employee_member: int, body: ItemEmployee):
    """
    *insert desc here

    :param id_employee_member: INT REQUIRED Id of the employee whose values are going to be updated
    :param body: OBJECT REQUIRED Contains all the updated values
    :return: JSON *insert here
    """

    res = put_employees(id_employee_member,
                        body.id_team,
                        body.family_name,
                        body.surname,
                        body.phone_number,
                        body.social_security_number,
                        body.emergency_contact)

    if res:
        return JSONResponse(
            status_code=200,
            content={"Message": "Table updated"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"Message": "Table not updated"}
        )

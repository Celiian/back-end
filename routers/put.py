from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from db.put import put_employees

router = APIRouter()


class Item(BaseModel):
    id_team: int | None
    family_name: str | None
    surname: str | None
    phone_number: str | None
    social_security_number: str | None
    emergency_contact: str | None


@router.get("/employees/{id}")
async def employees(id_employee_member: int, body: Item):
    id_team = body.id_team
    family_name = body.family_name
    surname = body.surname
    phone_number = body.phone_number
    social_security_number = body.social_security_number
    emergency_contact = body.emergency_contact

    res = put_employees(id_employee_member, id_team, family_name, surname, phone_number, social_security_number,
                        emergency_contact)

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

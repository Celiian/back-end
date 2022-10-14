from db.db_params import *
from exception_error.custom_exception import CustomError

def put_employees(id_employee_member, id_team, family_name, surname, phone_number, social_security_number,
                  emergency_contact):
    query = f"""UPDATE employees SET """
    comma = " "

    if id_team:
        query += comma+f"id_team={id_team}"
        comma = ", "
    if family_name:
        query += comma+f"family_name='{family_name}'"
        comma = ", "
    if surname:
        query += comma+f"surname='{surname}'"
        comma = ", "
    if phone_number:
        query += comma+f"phone_number='{phone_number}'"
        comma = ", "
    if social_security_number:
        query += comma+f"social_security_number='{social_security_number}'"
        comma = ", "
    if emergency_contact:
        query += comma+f"emergency_contact='{emergency_contact}'"

    query += f"WHERE id_employee_member = {id_employee_member};"

    print(query)
    res = update_data(query)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res



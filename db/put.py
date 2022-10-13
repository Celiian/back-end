from db.db_params import *


def put_employees(id_employee_member, id_team, family_name, surname, phone_number, social_security_number,
                  emergency_contact):
    query = """UPDATE employees
    SET id_team = %s
    AND family_name = %s
    AND surname = %s
    AND phone_number = %s
    AND social_security_number = %s
    AND emergency_contact = %s
    WHERE id_employee_member = %s
    """
    record = [id_employee_member]

    print(query)
    return selectData(query, record)



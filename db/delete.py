from db.db_params import *
from db.get import *
from exception_error.custom_exception import CustomError


def delete_enclosure(id):
    """
    Request for enclosures()

    :return: LIST The data from the database
    """
    query = (f"""
            DELETE FROM enclosures
            WHERE id_enclosure = %s
         """)

    record = [id]

    res = deleteData(query, record)
    return res


def delete_team(id):
    """
    Request for teams()

    :return: LIST The data from the database
    """
    if get_team_employees(id):
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "The team still have employees affected to itself",
            }
        )

    data = get_team(id)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "This team does not exist",
            }
        )

    query = (f"""       
    DELETE teams_organisations, teams FROM teams_organisations
    INNER JOIN teams
    ON teams.id_team = teams_organisations.id_team
    WHERE teams_organisations.id_team= %s;
            """)

    record = [id]
    res = deleteData(query, record)
    return res



def delete_food_supply(id):
    """
    Request for teams()

    :return: LIST The data from the database
    """

    data = get_breeds()
    for i in range(0, len(data)):
        if data[i][2] == id:
            raise CustomError(
                status_code=400,
                content=
                {
                    "error": "You can't delete a food supply used by a breed",
                }
            )

    data = get_food_supply(id)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "This food supply does not exist",
            }
        )

    query = (f"""       
            DELETE FROM food_supplies 
            WHERE food_type = %s
            """)

    record = [id]
    res = deleteData(query, record)
    return res




def delete_employees(id):
    """
    Request for employees()

    :return: LIST The data from the database
    """

    data = get_dinosaurs()
    for i in range(0, len(data)):
        if data[i][7] == id:
            raise CustomError(
                status_code=400,
                content=
                {
                    "error": "This employee is taking care of a dinosaur you can't fire him",
                }
            )


    data = get_team_employees(id)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "This employee does not exist",
            }
        )

    query = (f"""       
            DELETE FROM employees 
            WHERE id_employee_member = %s
            """)

    record = [id]
    res = deleteData(query, record)
    return res

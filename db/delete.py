from db.get import *
from exception_error.custom_exception import CustomError


def delete_enclosure(enclosure_id):
    """
    Request for enclosures()

    :param enclosure_id: INT REQUIRED Id of the enclosure
    :return: DICT The succes message is the query went well
    """


    data = get_dinosaurs()
    for i in range(0, len(data)):
        if data[i][2] == enclosure_id:
            raise CustomError(
                status_code=400,
                content=
                {
                    "Error": "You can't delete a enclosure where dinosaurs still live",
                }
            )

    if not get_enclosure(enclosure_id):
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "This id does not exist",
            }
        )
    query = (f"""
            DELETE FROM enclosures
            WHERE id_enclosure = %s
         """)

    record = [enclosure_id]

    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def delete_team(team_id):
    """
    Request for teams()

    :param team_id: INT REQUIRED Id of the team
    :return: DICT The succes message is the query went well
    """
    if get_team_employees(team_id):
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "The team still have employees affected to itself",
            }
        )

    data = get_team(team_id)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "This team does not exist",
            }
        )
    query = ""
    data = get_teams_organisation_team(team_id)
    if not data:
        query = (f"""       
           DELETE FROM teams
           WHERE id_team= %s;
                   """)

    else :
        query = (f"""       
        DELETE teams_organisations, teams FROM teams_organisations
        INNER JOIN teams
        ON teams.id_team = teams_organisations.id_team
        WHERE teams_organisations.id_team= %s;
                """)

    record = [team_id]
    res = delete_data(query, record)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    return res


def delete_food_supply(food_name):
    """
    Request for teams()

    :param food_name: STR REQUIRED Name of the food
    :return: DICT The succes message is the query went well
    """

    data = get_breeds()
    for i in range(0, len(data)):
        if data[i][2] == food_name:
            raise CustomError(
                status_code=400,
                content=
                {
                    "Error": "You can't delete a food supply used by a breed",
                }
            )

    data = get_food_supply(food_name)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "This food supply does not exist",
            }
        )

    query = (f"""       
            DELETE FROM food_supplies 
            WHERE food_type = %s
            """)

    record = [food_name]
    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    return res


def delete_employees(employee_id):
    """
    Request for employees()

    :param employee_id: INT REQUIRED Id of the employee
    :return: DICT The succes message is the query went well
    """

    data = get_dinosaurs()
    for i in range(0, len(data)):
        if data[i][7] == employee_id:
            raise CustomError(
                status_code=400,
                content=
                {
                    "Error": "This employee is taking care of a dinosaur you can't fire him",
                }
            )

    data = get_team_employees(employee_id)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "This employee does not exist",
            }
        )

    query = (f"""       
            DELETE FROM employees 
            WHERE id_employee_member = %s
            """)

    record = [employee_id]
    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    return res


def delete_dinosaurs(dinosaur_name):
    """
    Request for dinosaurs()

    :param dinosaur_name: STR REQUIRED Name of the dinosaur
    :return: DICT The succes message is the query went well
    """

    data = get_dinosaur(dinosaur_name)
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "Error": "This dinosaur does not exist",
            }
        )

    query = (f"""       
            DELETE FROM dinosaurs 
            WHERE dinosaur_name = %s
            """)

    record = [dinosaur_name]
    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    return res


def delete_breeds(breed_name):
    """
    Request for breeds()

    :param breed_name: STR REQUIRED Name of the breed
    :return: DICT The succes message is the query went well
    """

    data = get_dinosaurs()
    for i in range(0, len(data)):
        if data[i][1] == breed_name:
            raise CustomError(
                status_code=400,
                content=
                {
                    "Error": "There are still dinosaurs of this breed alive",
                }
            )

    data = get_breeds()
    if not data:
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "This breed does not exist",
            }
        )

    query = (f"""       
            DELETE FROM breeds 
            WHERE breed_name = %s
            """)

    record = [breed_name]
    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    
    return res


def delete_teams_organisation(id_team, id_enclosure):
    """
    Request for teams_organisation()

    :param id_team: INT REQUIRED id of the enclosure
    :param id_enclosure: INT REQUIRED id of the team
    :return: DICT The succes message is the query went well
    """

    data = get_team(id_team)
    if not data:
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "The team id does not exist",
            }
        )

    data = get_enclosure(id_enclosure)
    if not data:
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "The enclosure id does not exist",
            }
        )

    query = (f"""       
            DELETE FROM teams_organisations 
            WHERE id_team = %s and id_enclosure = %s
            """)

    record = [id_team, id_enclosure]
    res = delete_data(query, record)
    
    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )
    
    return res

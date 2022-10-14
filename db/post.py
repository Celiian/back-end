from __future__ import print_function
from db.db_params import insert_data
from exception_error.custom_exception import CustomError
# Connect with the MySQL Server
from db.get import *


def post_team_organisation(data):
    """
    Defines the query string, then calls insertData function using data and post_team_org_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """

    data_team = get_teams_organisations()

    for line in data_team:
        if line[0] == data[0] and line[1] == data[1]:
            raise CustomError(
                status_code=409,
                content=
                {
                    "Error": "This pair of id already exist",
                }
            )

    post_team_org_query = "INSERT INTO teams_organisations(id_enclosure, id_team) " \
                          "VALUES (%s,%s)"
    res = insert_data(post_team_org_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_team(data):
    """
    Defines the query string, then calls insertData function using data and post_breed_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_team_query = "INSERT INTO teams(team_type, vehicle_type) " \
                      "VALUES (%s,%s)"
    res = insert_data(post_team_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_food(data):
    """
    Defines the query string, then calls insertData function using data and post_food_query as parameter

    :param data: OBJECT REQUIRED Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """

    if get_food_supply(data[0]):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This food already exist",
            }
        )

    post_food_query = "INSERT INTO food_supplies(food_type, price) " \
                      "VALUES (%s,%s)"
    res = insert_data(post_food_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_breed(data):
    """
    Defines the query string, then calls insertData function using data and post_breed_query as parameter

    :param data: OBJECT REQUIRED Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """

    if get_breed(data[0]):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This breed already exist",
            }
        )

    post_breed_query = "INSERT INTO breeds(breed_name, food_eaten_daily, regime_type, era, biome_needed, price)" \
                       " VALUES (%s,%s,%s,%s,%s,%s)"
    res = insert_data(post_breed_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_dinosaur(data):
    """
    Defines the query string, then calls insertData function using data and post_dinosaur_query as parameter

    :param data: OBJECT REQUIRED Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """

    if get_food_supply(data[0]):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This dinosaur already exist",
            }
        )

    post_dinosaur_query = "INSERT INTO dinosaurs(dinosaur_name, breed_name, id_enclosure, creation_date, gender, height, weight, id_employees)" \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    res = insert_data(post_dinosaur_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_enclosure(data):
    """
    Defines the query string, then calls insertData function using data and post_enclosure_query as parameter

    :param data: OBJECT REQUIRED The tuple containing the values of biome and maintenance_cost
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_enclosure_query = "INSERT INTO enclosures(biome,maintenance_cost) " \
                           "VALUES (%s,%s)"
    res = insert_data(post_enclosure_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res


def post_employee(data):
    """
    Defines the query string, then calls insertData function using data and post_employee_query as parameter

    :param data: OBJECT REQUIRED The tuple containing the values of id_team, family_name,surname,phone_number,social_security_number,emergency_contact
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_employee_query = "INSERT INTO employees(id_team,family_name,surname,phone_number,social_security_number,emergency_contact) " \
                          "VALUES (%s,%s,%s,%s,%s,%s)"
    res = insert_data(post_employee_query, data)

    if res["error"] != "":
        raise CustomError(
            status_code=400,
            content={"Message": "Unexpected error",
                     "Error": res["error"]
                     }
        )

    return res

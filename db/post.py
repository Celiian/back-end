from __future__ import print_function
from db.db_params import insertData
# Connect with the MySQL Server


def postTeam(data):
    """
    Defines the query string, then calls insertData function using data and post_breed_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_team_query = "INSERT INTO teams(team_type, vehicle_type) VALUES (%s,%s)"
    res = insertData(post_team_query, data)

    return res


def postFood(data):
    """
    Defines the query string, then calls insertData function using data and post_breed_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_food_query = "INSERT INTO food_supplies(food_type, price) VALUES (%s,%s)"
    res = insertData(post_food_query, data)

    return res


def postBreed(data):
    """
    Defines the query string, then calls insertData function using data and post_breed_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_breed_query = "INSERT INTO breeds(breed_name, food_eaten_daily, regime_type, era, biome_needed, price) VALUES (%s,%s,%s,%s,%s,%s)"
    res = insertData(post_breed_query, data)

    return res


def postDinosaur(data):
    """
    Defines the query string, then calls insertData function using data and post_dinosaur_query as parameter

    :param data: OBJECT Containing all the values to insert in the query
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_dinosaur_query = "INSERT INTO dinosaurs(dinosaur_name, breed_name, id_enclosure, creation_date, gender, height, weigh, id_employees) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    res = insertData(post_dinosaur_query, data)

    return res

def postEnclosure(data):
    """
    Defines the query string, then calls insertData function using data and post_enclosure_query as parameter

    :param data: JSON The tuple containing the values of biome and maintenance_cost
    :return: BOOL The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_enclosure_query = "INSERT INTO enclosures(biome,maintenance_cost) VALUES (%s,%s)"
    res = insertData(post_enclosure_query, data)

    return res

def postEmployee(data):
    """
    Defines the query string, then calls insertData function using data and post_employee_query as parameter

    :param data: TUPLE REQUIRED The tuple containing the values of id_team, family_name,surname,phone_number,social_security_member,emergency_contact
    :return: The boolean value that becomes true if post succeeds or false if post fails.
    """
    post_employee_query = "INSERT INTO employees(id_team,family_name,surname,phone_number,social_security_member,emergency_contact) VALUES (%s,%s,%s,%s,%s,%s)"
    res = insertData(post_employee_query, data)

    return res

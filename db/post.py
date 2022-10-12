from __future__ import print_function
from db.db_params import insertData
# Connect with the MySQL Server

def postEnclosure(data):
    """
    Defines the query string, then calls insertData function using data and post_enclosure_query as parameter

    :param data: The tuple containing the values of biome and maintenance_cost
    :return: The boolean value that becomes true if post succeeds or false if post fails.
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



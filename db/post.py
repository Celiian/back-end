from __future__ import print_function
from db.db_params import insertData
# Connect with the MySQL Server

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
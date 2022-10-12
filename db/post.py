from __future__ import print_function
from db.db_param import insertData
# Connect with the MySQL Server


def postEnclosure(data):
    post_enclosure_query = "INSERT INTO enclosures(biome,maintenance_cost) VALUES (%s,%s)"
    res = insertData(post_enclosure_query, data)

    return res





from db.db_params import *


def patch_enclosures(id, cost, biome):
    """
    Function to edit cost or biome of an enclosure

    :param id: INT REQUIRED id of an enclosure
    :param cost: STRING OPTIONAL maintenance cost of an enclosure
    :param biome: STRING OPTIONAL biome of an enclosure
    :return: BOOLEAN Table updated or not
    """
    query = "UPDATE enclosures SET"
    record = []
    if cost is not None:
        record.append(cost)
        query += " maintenance_cost = %s"

    if biome is not None:
        if cost:
            query += ","
        record.append(biome)
        query += " biome = %s"
    record.append(id)
    query += " WHERE id_enclosure = %s"
    return update_data(query, record)

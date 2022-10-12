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


def patch_teams(id, team_type, vehicle_type):
    """
    Edit teams properties

    :param id: INT REQUIRED team id
    :param team_type: STRING OPTIONAL type of category of a team
    :param vehicle_type: STRING OPTIONAL type of vehicle for a team
    :return: BOOLEAN Table updated or not
    """
    query = "UPDATE teams SET"
    record = []
    if team_type:
        record.append(team_type)
        query += " team_type = %s"
    if vehicle_type:
        if team_type:
            query += ","
        record.append(vehicle_type)
        query += " vehicle_type = %s"
    record.append(id)
    query += " WHERE id_team = %s"
    return update_data(query, record)

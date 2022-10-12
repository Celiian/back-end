from db.db_params import *
from db.get import get_team


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


def patch_employees(id, id_team, family_name, phone_number, emergency_contact):
    """
    Edit employees informations

    :param id: INT REQUUIRED
    :param id_team: INT OPTIONAL
    :param family_name: STRING OPTIONAL
    :param phone_number: STRING OPTIONAL
    :param emergency_contact: STRING OPTIONAL
    :return: BOOLEAN Table updated or not
    """
    query = "UPDATE employees SET"
    record = []
    preceded = False
    if get_team(id_team):
        record.append(id_team)
        query += " id_team = %s"
        preceded = True

    if family_name:
        if preceded:
            query += ","
        record.append(family_name)
        query += " family_name = %s"
        preceded = True

    if phone_number:
        if preceded:
            query += ","
        record.append(phone_number)
        query += " phone_number = %s"
        preceded = True

    if emergency_contact:
        if preceded:
            query += ","
        record.append(emergency_contact)
        query += " emergency_contact = %s"
    record.append(id)
    query += "WHERE id_employee_member = %s"
    return update_data(query, record)

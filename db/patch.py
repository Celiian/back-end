from db.db_params import *
from db.get import get_enclosure, get_employee


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


def patch_dinosaurs(dinosaur_name, id_enclosure, gender, height, weight, id_employees):
    """
    Edit dinosaur's informations

    :param dinosaur_name: STRING REQUIRED dinosaur name
    :param id_enclosure: INT OPTIONAL dinosaur enclosure id
    :param gender: STRING OPTIONAL dinosaur gender
    :param height: INT OPTIONAL dinosaur height
    :param weight: INT OPTIONAL dinosaur weight
    :param id_employees: INT OPTIONAL dinosaur employee id
    :return: BOOLEAN Table updated or not
    """
    query = "UPDATE dinosaurs SET"
    record = []
    preceded = False

    if gender:
        record.append(gender)
        query += " gender = %s"
        preceded = True

    if get_enclosure(id_enclosure):

        if preceded:
            query += ","
        record.append(id_enclosure)
        query += " id_enclosure = %s"
        preceded = True

    if height:
        if preceded:
            query += ","
        record.append(height)
        query += " height = %s"
        preceded = True

    if weight:
        if preceded:
            query += ","
        record.append(weight)
        query += " weight = %s"
        preceded = True

    if get_employee(id_employees):
        if preceded:
            query += ","
        record.append(id_employees)
        query += " id_employees = %s"
    record.append(dinosaur_name)
    query += " WHERE dinosaur_name = %s"
    print(query)
    return update_data(query, record)

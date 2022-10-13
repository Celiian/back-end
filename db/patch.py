from db.get import *


def patch_enclosures(id_enclosure, cost, biome):
    """
    Function to edit cost or biome of an enclosure

    :param id_enclosure: INT REQUIRED id of an enclosure
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
    record.append(id_enclosure)
    query += " WHERE id_enclosure = %s"
    return update_data(query, record)


def patch_breeds(name, food_eaten_daily, regime_type, era, biome_needed, price):
    """
    Edit breed information

    :param name: STRING REQUIRED breed name
    :param food_eaten_daily: INT OPTIONAL quantity of food eaten daily
    :param regime_type: STRING OPTIONAL breed regime type
    :param era: STRING OPTIONAL breed living era
    :param biome_needed: STRING OPTIONAL breed biome needed
    :param price: INT OPTIONAL breed price (/kg)
    :return: BOOLEAN Table updated or not
    """
    query = "UPDATE breeds SET"
    record = []
    preceded = False

    if food_eaten_daily:
        record.append(food_eaten_daily)
        query += " food_eaten_daily = %s"
        preceded = True

    if get_food_supply(regime_type):
        if preceded:
            query += ","
        record.append(regime_type)
        query += " regime_type = %s"
        preceded = True

    if era:
        if preceded:
            query += ","
        record.append(era)
        query += " era = %s"
        preceded = True

    if biome_needed:
        if preceded:
            query += ","
        record.append(biome_needed)
        query += " biome_needed = %s"
        preceded = True

    if price:
        if preceded:
            query += ","
        record.append(price)
        query += " price = %s"

    record.append(name)
    query += " WHERE breed_name = %s"
    return update_data(query, record)


def patch_dinosaurs(dinosaur_name, id_enclosure, gender, height, weight, id_employees):
    """
    Edit dinosaur's information

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

    print(gender, weight, dinosaur_name)

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


def patch_employees(id_employee, id_team, family_name, phone_number, emergency_contact):
    """
    Edit employees information

    :param id_employee: INT REQUIRED
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
    record.append(id_employee)
    query += " WHERE id_employee_member = %s"
    print(query)
    return update_data(query, record)


def patch_teams(id_team, team_type, vehicle_type):
    """
    Edit teams properties

    :param id_team: INT REQUIRED team id
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
    record.append(id_team)
    query += " WHERE id_team = %s"
    print(query)
    return update_data(query, record)


def patch_teams_orga(id_enclosure, id_team, new_id_enclosure, new_id_team):
    """
    Edit the link between a team and an enclosure

    :param id_enclosure: INT REQUIRED table id that can be replaced
    :param id_team: INT REQUIRED table id that can be replaced
    :param new_id_enclosure: INT OPTIONAL the new id to be put in the table
    :param new_id_team: INT OPTIONAL the new id to be put in the table
    :return: BOOLEAN Table updated or not
    """

    query = "UPDATE teams_organisations SET"
    record = []
    if get_teams_organisation_team(new_id_team):
        record.append(new_id_team)
        query += " id_team = %s"

    if get_teams_organisation_enclosure(new_id_enclosure):
        record.append(new_id_enclosure)
        query += " id_enclosure = %s"

    if get_teams_organisation_team(id_team) and get_teams_organisation_enclosure(id_enclosure):

        record.append(id_enclosure)
        query += " WHERE id_enclosure = %s"
        record.append(id_team)
        query += " AND id_team = %s"
    print(query)
    return update_data(query, record)



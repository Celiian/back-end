from db.get import *
from exception_error.custom_exception import CustomError


def patch_enclosures(id_enclosure, cost, biome):
    """
    Function to edit cost or biome of an enclosure

    :param id_enclosure: INT REQUIRED id of an enclosure
    :param cost: STRING OPTIONAL maintenance cost of an enclosure
    :param biome: STRING OPTIONAL biome of an enclosure
    :return: BOOLEAN Table updated or not
    """

    if not get_enclosure(id_enclosure):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )

    query = "UPDATE enclosures SET"
    record = []
    if cost:
        record.append(cost)
        query += " maintenance_cost = %s"

    if biome:
        if cost:
            query += ","
        record.append(biome)
        query += " biome = %s"

    if biome is None and cost is None:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

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

    if not get_breed(name):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This name does not exist",
            }
        )

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

    if food_eaten_daily is None and regime_type is None and era is None and biome_needed is None and price is None:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

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

    if not get_dinosaur(dinosaur_name):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )

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

    if id_enclosure is None and gender is None and height is None and weight is None and id_employees is None:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

    record.append(dinosaur_name)
    query += " WHERE dinosaur_name = %s"
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

    if not get_employee(id_employee):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )

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

    if id_team is None and family_name is None and phone_number is None and emergency_contact is None:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

    record.append(id_employee)
    query += " WHERE id_employee_member = %s"
    print(query)
    print(record)
    return update_data(query, record)


def patch_teams(id_team, team_type, vehicle_type):
    """
    Edit teams properties

    :param id_team: INT REQUIRED team id
    :param team_type: STRING OPTIONAL type of category of a team
    :param vehicle_type: STRING OPTIONAL type of vehicle for a team
    :return: BOOLEAN Table updated or not
    """


    if not get_team(id_team):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )

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

    if team_type is None and vehicle_type is None:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

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


    if not get_enclosure(id_enclosure):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )


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
    return update_data(query, record)


def patch_food_supplies(food_type, price):
    """
    Edit food supplies price

    :param food_type: STRING REQUIRED type of food
    :param price: STRING REQUIRED food price (/kg)
    :return: BOOLEAN Table updated or not
    """

    if not get_food_supply(food_type):
        raise CustomError(
            status_code=409,
            content=
            {
                "Error": "This id does not exist",
            }
        )


    query = "UPDATE food_supplies SET"
    record = []
    if price:
        record.append(price)
        query += " price = %s"
    else:
        raise CustomError(
            status_code=409,
            content={"Message": "Please choose an existing value"}
        )

    record.append(food_type)
    query += " WHERE food_type = %s"

    return update_data(query, record)

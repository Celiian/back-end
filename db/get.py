import datetime

from db.db_params import *
from datetime import date


def formate_date(data):
    """
    This function will change the type of the date (datetime.date) in a tuple
    (by sending the new values in another tuple)

    :param data: TUPLE OR LIST REQUIRED The tuple
    :return: TUPLE The new tuple
    """
    new_data = []
    for i in range(0, len(data)):
        temp_data = []
        for y in range(0, len(data[i])):
            if type(data[i][y]) == datetime.date:
                temp_data.append(date.isoformat(data[i][y]))
            else:
                temp_data.append(data[i][y])

        new_data.append(temp_data)
    return new_data


def get_enclosures():
    """
    Request for enclosures()

    :return: LIST The data from the database
    """
    query = (f"""
       SELECT * FROM enclosures
         """)

    data = select_data(query)

    return data


def get_enclosure(id):
    """
     Request for enclosure()

    :param id: INT REQUIRED The id of the enclosure
    :return: LIST The data from the database
    """
    query = (f"""
          SELECT * FROM enclosures
          WHERE id_enclosure = %s
            """)
    record = [id]

    data = select_data(query, record)

    return data


def get_enclosure_dinosaurs(id):
    """
    Request for enclosure_dinosaurs()

    :param id: INT REQUIRED The id of the enclosure
    :return: LIST The data from the database
    """
    query = (f"""
          SELECT * FROM dinosaurs
          WHERE id_enclosure = %s
            """)
    record = [id]
    data = select_data(query, record)
    new_data = formate_date(data)

    return new_data


get_enclosure_dinosaurs(2)


def get_enclosure_teams(id):
    """
    Request for enclosure_teams()

    :param id: INT REQUIRED The id of the enclosure
    :return: LIST The data from the database
    """
    query = (f"""
          SELECT teams.* FROM teams, teams_organisations
          WHERE id_enclosure = %s AND teams.id_team = teams_organisations.id_team
            """)
    record = [id]

    data = select_data(query, record)

    return data


def get_enclosure_teams_employees(id):
    """
    Request for enclosure_teams_employees()

    :param id: INT REQUIRED The id of the enclosure
    :return: LIST The data from the database
    """
    query = (f"""
          SELECT employees.* FROM employees, teams, teams_organisations
          WHERE id_enclosure = %s
            AND teams.id_team = teams_organisations.id_team
            AND employees.id_team = teams_organisations.id_team
            """)
    record = [id]

    data = select_data(query, record)

    return data


def get_teams():
    """
    Request for teams()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams
                """)

    data = select_data(query)

    return data


def get_team(id):
    """
    Request for team()

    :param id: INT REQUIRED The id of the team
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams
              WHERE id_team = %s
                """)

    record = [id]
    data = select_data(query, record)

    return data


def get_team_employees(id):
    """
    Request for team_employees()

    :param id: INT REQUIRED The id of the team
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees, teams
              WHERE teams.id_team = %s 
              AND teams.id_team = employees.id_team
                """)

    record = [id]
    data = select_data(query, record)

    return data


def get_team_enclosures(id):
    """
    Request for team_enclosures()

    :param id: INT REQUIRED The id of the team
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT enclosures.* FROM enclosures, teams, teams_organisations
              WHERE teams.id_team = %s 
              AND teams_organisations.id_team = teams.id_team
              AND teams_organisations.id_enclosure = enclosures.id_enclosure
              
                """)

    record = [id]
    data = select_data(query, record)

    return data


def get_employees():
    """
    Request for employees()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees
                """)

    data = select_data(query)

    return data


def get_employee(id):
    """
    Request for employee()

    :param id: INT REQUIRED The id of the employee
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees
               WHERE id_employee_member = %s
                """)

    record = [id]
    data = select_data(query, record)

    return data

def get_food_supplies():
    """
    Request for food_supplies()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT food_supplies.* FROM food_supplies
                """)

    data = select_data(query)

    return data


def get_food_supply(food_type):
    """
    Request for food_supply()

    :param id: INT REQUIRED The id of the food_supply
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT food_supplies.* FROM food_supplies
               WHERE food_type = %s
                """)

    record = [food_type]
    data = select_data(query, record)

    return data


def get_dinosaurs():
    """
    Request for dinosaurs()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT dinosaurs.* FROM dinosaurs
                """)

    data = select_data(query)

    new_data = formate_date(data)
    return new_data


def get_dinosaur(name):
    """
    Request for dinosaurs()

    :param name: STR REQUIRED The name of the dinosaur
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT dinosaurs.* FROM dinosaurs
              WHERE dinosaur_name = %s
                """)

    record = [name]
    data = select_data(query, record)

    new_data = formate_date(data)
    return new_data


def get_dinosaur_breed(name):
    """
    Request for dinosaurs()

    :param name: STR REQUIRED The name of the dinosaur
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT breeds.* FROM dinosaurs, breeds
              WHERE dinosaur_name = %s
              AND dinosaurs.breed_name = breeds.breed_name
                """)

    record = [name]
    data = select_data(query, record)

    return data




def get_breeds():
    """
    Request for breeds()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT breeds.* FROM breeds
                """)

    data = select_data(query)

    return data


def get_breed(name):
    """
    Request for breed()

    :param name: STR REQUIRED The name of the breed
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT breeds.* FROM breeds
              WHERE breed_name = %s
                """)

    record = [name]
    data = select_data(query, record)

    return data





def get_teams_organisations():
    """
    Request for teams_organisations()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams_organisations
                """)

    data = select_data(query)

    return data


def get_teams_organisation_team(id_team):
    """
    Request for teams_organisation_team()

    :param id_team: INT REQUIRED The id of the team
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams_organisations
              WHERE id_team = %s
                """)

    record = [id_team]
    data = select_data(query, record)

    new_data = formate_date(data)
    return new_data



def get_teams_organisation_enclosure(id_enclosure):
    """
    Request for teams_organisation_team()

    :param id_enclosure: INT REQUIRED The id of the enclosure
    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams_organisations
              WHERE id_enclosure = %s
                """)

    record = [id_enclosure]
    data = select_data(query, record)

    new_data = formate_date(data)
    return new_data

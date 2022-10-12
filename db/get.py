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

    data = selectData(query)

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

    data = selectData(query, record)

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
    data = selectData(query, record)
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

    data = selectData(query, record)

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

    data = selectData(query, record)

    return data


def get_teams():
    """
    Request for teams()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams
                """)

    data = selectData(query)

    return data


def get_team(id):
    """
    Request for team()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT * FROM teams
              WHERE id_team = %s
                """)

    record = [id]
    data = selectData(query, record)

    return data


def get_team_employees(id):
    """
    Request for team_employees()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees, teams
              WHERE teams.id_team = %s 
              AND teams.id_team = employees.id_team
                """)

    record = [id]
    data = selectData(query, record)

    return data


def get_team_enclosures(id):
    """
    Request for team_enclosures()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT enclosures.* FROM enclosures, teams, teams_organisations
              WHERE teams.id_team = %s 
              AND teams_organisations.id_team = teams.id_team
              AND teams_organisations.id_enclosure = enclosures.id_enclosure
              
                """)

    record = [id]
    data = selectData(query, record)

    return data


def get_employees():
    """
    Request for employees()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees
                """)

    data = selectData(query)

    return data


def get_employee(id):
    """
    Request for employee()

    :return: LIST The data from the database
    """
    query = (f"""
              SELECT employees.* FROM employees
               WHERE id_employee_member = %s
                """)

    record = [id]
    data = selectData(query, record)

    return data


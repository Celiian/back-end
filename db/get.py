import datetime

from db.db_params import *
from datetime import date
def formate_date(data):
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
    query = (f"""
       SELECT * FROM enclosures
         """)

    data = selectData(query)

    return data


def get_enclosure(id):
    query = (f"""
          SELECT * FROM enclosures
          WHERE id_enclosure = %s
            """)
    record = [id]

    data = selectData(query, record)

    return data


def get_enclosure_dinosaurs(id):
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
    query = (f"""
          SELECT teams.* FROM teams, teams_organisations
          WHERE id_enclosure = %s AND teams.id_team = teams_organisations.id_team
            """)
    record = [id]

    data = selectData(query, record)

    return data

def get_enclosure_teams_employees(id):
    query = (f"""
          SELECT employees.* FROM employees, teams, teams_organisations
          WHERE id_enclosure = %s
            AND teams.id_team = teams_organisations.id_team
            AND employees.id_team = teams_organisations.id_team
            """)
    record = [id]

    data = selectData(query, record)

    return data


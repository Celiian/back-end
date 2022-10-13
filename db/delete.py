from db.db_params import *
from db.get import *
from exception_error.custom_exception import CustomError


def delete_enclosure(id):
    """
    Request for enclosures()

    :return: LIST The data from the database
    """
    query = (f"""
            DELETE FROM enclosures
            WHERE id_enclosure = %s
         """)

    record = [id]

    res = deleteData(query, record)
    return res


def delete_team(id):
    """
    Request for teams()

    :return: LIST The data from the database
    """
    if get_team_employees(id):
        raise CustomError(
            status_code=400,
            content=
            {
                "error": "The team still have employees affected to itself",
            }
        )

    query = (f"""       
    DELETE teams_organisations, teams FROM teams_organisations
    INNER JOIN teams
    ON teams.id_team = teams_organisations.id_team
    WHERE teams_organisations.id_team= %s;
            """)

    record = [id]
    res = deleteData(query, record)
    return res

from db.db_params import *


def delete_enclosures(id):
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

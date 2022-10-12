import mysql.connector as mc
from password import returnPassword


def selectData(query, record = None):
    """
    connect to the database and perform a query
    :param query:STRING REQUIRED the query to be made
    :param record: STRING OPTIONAL
    :return: LIST all the data from the query
    """
    password = returnPassword()

    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()
    result = []
    my_cursor.execute(query, record)
    for i in my_cursor:
        result.append(i)
    return result

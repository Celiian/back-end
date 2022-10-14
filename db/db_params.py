import mysql.connector as mc
from password import returnPassword

password = returnPassword()


def update_data(query):
    """
    Connect to the database and perform a query

    :param query: STRING REQUIRED the query to be made
    :return:  BOOLEAN True if the query is done False if there is a problem
    """
    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()
    try:
        my_cursor.execute(query)
        db.commit()
        return True
    except mc.Error:
        return False


def select_data(query, record=None):
    """
    Connect to the database and perform a query

    :param query: STRING REQUIRED the query to be made
    :param record: STRING OPTIONAL
    :return: LIST all the data from the query
    """

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


def insert_data(query, record):
    """
          connect to the database and perform a query

          :param query:STRING REQUIRED the query to be made
          :param record: STRING OPTIONAL
          :return: BOOLEAN True if the query is done False if there is a problem
      """
    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()
    try:
        my_cursor.execute(query, record)
        db.commit()
        return True
    except mc.Error as error:
        print(error)
        return False


def delete_data(query, record=None):
    """
    connect to the database and perform a query

    :param query:STRING REQUIRED the query to be made
    :param record: STRING OPTIONAL
    :return:  BOOLEAN True if the query is done False if there is a problem
    """

    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()
    res = {
        "message": "",
        "error": ""
    }
    try:
        my_cursor.execute(query, record)
        db.commit()
        res["message"] = "Deleted successfully"
        return res
    except mc.Error as error:
        res["message"] = "Error"
        res["error"] = error.msg
        return res

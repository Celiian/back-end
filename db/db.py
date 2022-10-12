import mysql.connector as mc
from password import returnPassword


def returnDb():
    password = returnPassword()

    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()

    return my_cursor

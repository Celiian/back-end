import mysql.connector as mc
from password import returnPassword


def update_data(query, record):
    password = returnPassword()
    db = mc.connect(user='root',
                    password=password,
                    host='127.0.0.1',
                    database='jurassic')

    my_cursor = db.cursor()
    try:
        my_cursor.execute(query, record)
        db.commit()
        return True
    except mc.Error:
        return False

import mysql.connector as mc
from password import returnPassword


def selectData(query, record = None):
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

def updateData(query, record):
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
    except mc.Error as error:
        print(error)
        return False

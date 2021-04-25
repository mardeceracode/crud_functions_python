from _db import db
from _messages import *

def show_data():
    if len(db) > 0:
        for user in db:
            print(
                separator_line_db,
                inprint, 'ID: ', user['id'], '\r',
                inprint, 'NOMBRE: ', user['name'], '\r',
                inprint, 'EDAD: ', user['age'], '\r',
                inprint, 'EMAIL: ', user['email'], '\r',
                separator_line_db
            )
    else:
        print(msn_db_void)
    print(separator_line)
from _db import db
from _messages import *

def search_data():
    catch = False
    name = input(msn_name_input)
    for user in db:
        if user['name'] == name:
            catch = True
            # for element in user:
            #     # print(f'-> {user[element]}')
            #     print(inprint, user[element])
            print(
                inprint, 'ID: ', user['id'], '\r',
                inprint, 'NOMBRE: ', user['name'], '\r',
                inprint, 'EDAD: ', user['age'], '\r',
                inprint, 'EMAIL: ', user['email']
            )
    if not catch:
        print(msn_not_exist)
    print(separator_line)
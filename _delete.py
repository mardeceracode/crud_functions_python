from _db import db
from _messages import *

def delete_data():
    catch = False
    try:
        id = int(input(msn_id_input))
        for user in db:
            if user['id'] == id:
                catch = True
                db.remove(user)
                print(msn_succesuful)
                break
        if not catch:
            print(msn_not_exist)
    except:
        print(msn_id_not_valid)
    
    print(separator_line)
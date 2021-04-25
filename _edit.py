from _db import db
from _messages import *

def edit_data():
    catch = False
    try:
        id = int(input(msn_id_input))
        for user in db:
            if user['id'] == id:
                catch = True
                while True:
                    try:
                        seleccted = int(input(
                            msn_edit_sub_menu
                        ))
                        if seleccted == 1:
                            new_name = input(msn_new_name)
                            user['name'] = new_name
                        elif seleccted == 2:
                            new_age = input(msn_new_age)
                            user['age'] = new_age
                        elif seleccted == 3:
                            new_email = input(msn_new_email)
                            user['email'] = new_email
                        elif seleccted == 4:
                            break
                    except:
                        print(msn_option_not_valid)
                break
        if not catch:
            print(msn_not_exist)
    except:
        print(msn_id_not_valid)
    print(separator_line)

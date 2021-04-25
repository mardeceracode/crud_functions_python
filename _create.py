from _db import db
from _messages import *

def get_data():
    try:
        id = int(input(msn_id_input))
        name = input(msn_name_input)
        age = int(input(msn_age_input))
        email = input(msn_email_input)

        create(id, name, age, email)
    
    except:
        print(msn_error_input)
    
    print(separator_line)


def create(id ,name, age, email):
    person = {
        'id': id,
        'name': name,
        'age': age,
        'email': email,
    }
    db.append(person)
import os
import datetime

def check_user():
    return os.system('whoami')

def check_system():
     return os.system('systeminfo')

def check_date():
    return os.system('date')

def date():
    return datetime.datetime.now()

date = date()
print(date)    
# check_system()
# check_user()
# check_date()
    
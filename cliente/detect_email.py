import re

regex= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def detect_email(email):
    if(re.search(regex,email)):
        return True
    else:
        return False
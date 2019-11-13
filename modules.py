# core modules
import datetime
from datetime import date
import time
from time import time

# pip module
import camelcase
from camelcase import CamelCase

# Import custom module
import validator
#from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

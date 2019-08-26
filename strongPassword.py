"""
Write a function that uses regex's to make sure the password string it is
passed is strong (meaning it is at least eight characters long, contains both
uppercase and lowercase characters, and has at least one digit).
"""

import re

def strongPass(password):
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    dig = re.compile(r'[0-9]')

    if len(password) < 8:
        print(('Your password is not strong enough - must be at least eight '
            'characters long'))

    elif lower.search(password) == None:
        print(('Your password is not strong enough - must contain at least '
            'one lowercase character'))

    elif upper.search(password) == None:
        print(('Your password is not strong enough - must contain at least '
            'one uppercase character'))

    elif dig.search(password) == None:
        print(('Your password is not strong enough - must contain at least '
            'one digit'))

    else:
        print('Your password is strong!')

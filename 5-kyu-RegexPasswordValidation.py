'''
You need to write regex that will validate a password to make sure it meets the following criteria:

- At least six characters long
- contains a lowercase letter
- contains an uppercase letter
- contains a number
- Valid passwords will only be alphanumeric characters.
'''

#Solution:

import re
def validation(password):

    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$", password):
        return True
    else:
        return False

# email_validator.py

import re

def is_valid_email(email):
    """
    Preveri, ali je e-poštni naslov veljaven.
    Veljaven e-poštni naslov vsebuje znake pred @, domeno in končnico.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

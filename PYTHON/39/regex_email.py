# regex_email.py

# text@text.com

import re

rx_email = re.compile(r'.+@[a-z0-9-\.]+\.[a-z0-9]{2,10}')

email = input('Zadejte email: ')


if rx_email.match(email):
    # toto vrací None nebo Match objekt
    print('Zdali jste validní email')
else:
    print('Nevalidní email')


"""
User auth. system
jmeno, příjmení
email, telefon

username
heslo
"""

users = {
    'suche': 'heslo',
    'jan': 'heslo2',
    'jana': 'heslo3',
    # 'suche': {'username': 'suche', 'password': 'heslo', 'id': 1},
}

"""
funkce nebo činnost:
- přidání nového uživatele
- kontrola hesla
- odebraní
- změna hesla/username
- oveření zda username existuje
"""


def add_user(username: str, password: str):
    """
    1. zkontrolovat zda neexistuje
    2. přidat username a heslo do users
    """

    if user_exists(username):
        raise ValueError('user already exists')
    
    users[username] = password
    

def password_check(username: str, password: str) -> bool:
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané vrátíme True
    3. jinak False
    """


def remove_user(username: str, password: str):
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané odebereme uživatele z users
    3. jinak vyhodíme chybu
    """


def user_exists(username: str) -> bool:
    return username in users    


def change_password(username: str, old_password: str, new_password: str):
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané tak nastavavíme nové heslo
    3. jinak vyhodíme chybu
    """



add_user('jan', 'Heslo1234')
print(users)

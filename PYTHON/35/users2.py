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
        raise ValueError('User already exists')
    
    users[username] = password
    

def password_check(username: str, password: str) -> bool:
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané vrátíme True
    3. jinak False
    """

    if user_exists(username):
        existing_password = users[username]
        return existing_password == password

    raise ValueError('User not exists')


def remove_user(username: str, password: str):
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané odebereme uživatele z users
    3. jinak vyhodíme chybu
    """
    if password_check(username, password):
        del users[username]
    else:
        raise ValueError('Invalid password')


def user_exists(username: str) -> bool:
    return username in users    


def change_password(username: str, old_password: str, new_password: str):
    """
    1. získáme heslo z users podle username
    2. pokud získané heslo je stejné jako zadané tak nastavavíme nové heslo
    3. jinak vyhodíme chybu
    """

    if password_check(username, old_password):
        users[username] = new_password # natavuji pro klíč [username] hodnotu [new_password]

        # x = users[username] # získávám hodnotu pro klíč [username] a ukládám do x
    else:
        raise ValueError('Invalid password')




print(password_check('suche', 'heslo_xyz'))
print(password_check('suche', 'heslo'))

change_password('suche', 'heslo1', 'new_password!!!')

print(users)

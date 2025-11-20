import json

from users import (
    users,
    add_user,
    password_check,
)


def save_data():
    file = open('python/35/users.json', mode='w', encoding='utf-8')
    json.dump(users, file)
    file.close()


def read_data():
    try:
        file = open('python/35/users.json', mode='r', encoding='utf-8')
        data = json.load(file)
        file.close()
        return data
    except json.JSONDecodeError:
        return {}


def main():
    data = read_data()
    users.update(data)

    add_user('pepa', 'heslo1234')
    print(users)

    save_data()

main()


"""
sklad = sklad1(Praha 9, Kaufland)
sklad = sklad2(Pardubice, Kaufland)
"""


actual_number = 0
max_number = 999


def command_exit():
    print('Ukončuji program')
    exit()

def command_reset():
    # global se znažíme vyhnout
    global actual_number
    print('Resetuji pořadník')

    actual_number = 0

def command_next():
    # global se znažíme vyhnout
    global actual_number
    global max_number

    if actual_number < max_number:
        actual_number += 1
    else:
        actual_number = 1

    print('Dostaváte číslo:', actual_number)


while True:
    command = input('Zadejte příkaz: ')

    if command == 'exit':
        command_exit()
    elif command == 'reset':
        command_reset()
    elif command == 'next':
        command_next()
    else:
        print('Zadal/a jste neznámý příkaz')
    
